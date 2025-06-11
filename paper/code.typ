#let load_code(path, language, start, stop) = {
  let full_code = read(path)
  let lines = full_code.split("\n")
  // raw(full_code, lang: language)
  let recording = false
  let start_line = 0
  let end_line = -1
  let line_no = 0
  while line_no < lines.len() {
    let line = lines.at(line_no)
    if start_line == 0 and line.starts-with(start) {
      start_line = line_no
    } else if end_line == -1 and line.starts-with(stop) {
      end_line = line_no
      break
    }
    line_no += 1
  }
  let code = lines.slice(start_line, end_line).join("\n")
  raw(code, lang: language)
}
