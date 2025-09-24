<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Site Map</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <style>
          /* Reset some default browser styles */
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }

          body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f4f8;
            padding: 20px;
            color: #333;
            line-height: 1.6;
          }

          h1 {
            font-size: 2rem;
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            color: #1a202c;
          }

          h1::before {
            content: "🗺️";
            margin-right: 10px;
          }

          .url {
            margin-bottom: 24px;
            padding: 16px;
            border-radius: 8px;
            background: #ffffff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s, box-shadow 0.2s;
          }

          .url:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
          }

          a {
            font-size: 1.1rem;
            color: #0073e6;
            text-decoration: none;
            font-weight: 500;
            display: inline-block;
            margin-bottom: 6px;
          }

          a:hover {
            text-decoration: underline;
          }

          small {
            color: #666;
            font-size: 0.9rem;
          }

          @media (max-width: 600px) {
            body {
              padding: 10px;
            }

            h1 {
              font-size: 1.5rem;
            }

            a {
              font-size: 1rem;
            }

            .url {
              padding: 12px;
            }
          }
        </style>
      </head>
      <body>
        <h1>Site Map</h1>
        <xsl:for-each select="//s:url">
          <div class="url">
            <a href="{s:loc}">
              <xsl:call-template name="format-title">
                <xsl:with-param name="loc" select="s:loc"/>
              </xsl:call-template>
            </a><br/>
            <small>Last Updated: <xsl:value-of select="s:lastmod"/></small>
          </div>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>

  <xsl:template name="format-title">
    <xsl:param name="loc"/>
    <xsl:variable name="title" select="substring-after($loc, '/blogdetail/')"/>
    <xsl:value-of select="translate($title, '-', ' ')"/>
  </xsl:template>

</xsl:stylesheet>
