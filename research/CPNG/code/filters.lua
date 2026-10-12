function Div(el)
  if el.classes:includes("pagebreak") then
    if FORMAT:match("docx") then
      return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    else
      return pandoc.RawBlock("html", '<div class="pagebreak"></div>')
    end
  end
  return el
end
