/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows == 1) return s;
  let output = [];

  for (let i = 0; i < numRows; ++i) {
    output.push("");
  }

  let rowCounter = 0;
  let angleCounter = 0;
  for (let i = 0; i < s.length; ++i) {
    if (rowCounter <= numRows - 1) {
      output[rowCounter] += s[i];
      ++rowCounter;
    } else {
      if (numRows === 2) {
        --i;
        rowCounter = 0;
        continue;
      }
      output[numRows - angleCounter - 2] += s[i];
      ++angleCounter;

      if (angleCounter >= numRows - 2) {
        angleCounter = 0;
        rowCounter = 0;
      }
    }
  }

  let outputS = "";
  for (let i = 0; i < numRows; ++i) {
    outputS += output[i];
  }
  return outputS;
};
