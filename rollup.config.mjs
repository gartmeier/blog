import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";

export default {
  input: "blog/static/main.js",
  output: {file: "blog/static/dist/main.js"},
  plugins: [resolve(), commonjs()],
};
