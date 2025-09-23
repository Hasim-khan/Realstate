<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html>
      <head>
        <title>Sitemap</title>
        <style>
          body { font-family: Arial; background: #f9f9f9; padding: 40px; }
          h1 { color: #333; }
          .url { margin: 10px 0; }
          a { color: #0073e6; text-decoration: none; }
          a:hover { text-decoration: underline; }
        </style>
      </head>
      <body>
        <h1>🗺️ Sitemap</h1>
        <xsl:for-each select="urlset/url">
          <div class="url">
            <a href="{loc}"><xsl:value-of select="loc"/></a><br/>
            <small>Last Modified: <xsl:value-of select="lastmod"/></small>
          </div>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>