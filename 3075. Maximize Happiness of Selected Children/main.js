/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function (happiness, k) {
  happiness.sort((a, b) => a - b);
  let totHappiness = 0;

  for (let i = 0; i < k; ++i) {
    let num = happiness.pop();
    totHappiness += num - i <= 0 ? 0 : num - i;
  }

  return totHappiness;
};
