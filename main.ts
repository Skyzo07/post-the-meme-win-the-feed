// "Post the Meme, Win the Feed" — entry program (Node 22, stdlib only).
// The entry is the X post itself: the meme image (meme.png, made in this
// session by render_meme.py) is posted natively on X from a public account,
// and POST.json at the repo root names that post. This program's only job
// is to hand POST.json to the grader: copy it from the repo root to the
// output directory and check it is a JSON object with a string url.
// It prints nothing on success and exits non-zero on any failure, so a
// broken POST.json fails loudly instead of silently scoring 0.
//
// Local check (mirrors the grader's env vars):
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const SOURCE = join(BOT_DIR, "POST.json");
const DEST = join(OUTPUT_DIR, "POST.json");

function fail(message: string): never {
  console.error(`main.ts: ${message}`);
  process.exit(1);
}

// Validate first, so a malformed POST.json is caught here, not by the gate.
let parsed: unknown;
try {
  parsed = JSON.parse(readFileSync(SOURCE, "utf8"));
} catch (err) {
  fail(`POST.json could not be parsed: ${(err as Error).message}`);
}
if (
  typeof parsed !== "object" ||
  parsed === null ||
  Array.isArray(parsed) ||
  typeof (parsed as { url?: unknown }).url !== "string"
) {
  fail("POST.json must be a JSON object with a string url field");
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(SOURCE, DEST);
} catch (err) {
  fail(`POST.json could not be copied to ${DEST}: ${(err as Error).message}`);
}
// Success: print nothing.

