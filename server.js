import express from 'express'
import path from 'node:path'
import { fileURLToPath } from 'url'

const app = express()
const port = 5173
//3000
// __dirname and __filename are not available in ES modules by default, so we need to recreate them
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

// Serve the .vue file
app.get('/download/:fileName', (req, res) => {
  const fileName = req.params.fileName
  const filePath = path.join(__dirname, 'src/components/AllComponentFolder', fileName)

  res.download(filePath, (err) => {
    if (err) {
      console.error('Error downloading file:', err)
      res.status(500).send('Error downloading the file')
    }
  })
})

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`)
})
