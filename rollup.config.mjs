import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import terser from "@rollup/plugin-terser";

export default {
  input: "blog/static/tiptap.js",
  output: {
    file: "blog/static/dist/tiptap.js",
    format: "iife",
    name: "tiptap",
    sourcemap: true,
  },
  plugins: [resolve(), commonjs(), terser()],
};
