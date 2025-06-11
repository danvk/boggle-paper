#let from_src(path, language: "python", start: "# Listing", stop: "# /Listing") = {
  let full_code = read(path)
  let lines = full_code.split("\n")
  // raw(full_code, lang: language)
  let recording = false
  let start_line = -1
  let end_line = -1
  let line_no = 0
  while line_no < lines.len() {
    let line = lines.at(line_no)
    if start_line == -1 and line.contains(start) {
      start_line = line_no
    } else if start_line >= 0 and line.contains(stop) {
      end_line = line_no
      break
    }
    line_no += 1
  }
  let code = lines.slice(start_line, end_line).join("\n")
  // Could wrap in figure or #block(raw(), breakable: false)
  raw(code, lang: language)
}
