import { Editor } from "@tiptap/core";
import StarterKit from "@tiptap/starter-kit";
import CodeBlockLowlight from "@tiptap/extension-code-block-lowlight";
import { common, createLowlight } from "lowlight";

let lowlight = createLowlight(common);

document.querySelectorAll(".tiptap-container").forEach((containerElement) => {
  let editorElement = containerElement.querySelector(".tiptap-editor");
  let inputElement = containerElement.querySelector('input[type="hidden"]');

  let editor = new Editor({
    element: editorElement,
    extensions: [
      StarterKit.configure({
        codeBlock: false,
      }),
      CodeBlockLowlight.configure({
        lowlight,
      }),
    ],
    editorProps: {
      attributes: {
        class: "prose textarea textarea-bordered max-w-none min-h-[250px]",
      },
    },
    content: inputElement.value,
    onUpdate: ({ editor }) => (inputElement.value = editor.getHTML()),
  });
});
