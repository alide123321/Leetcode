/**
 * @param {string[]} code
 * @param {string[]} businessLine
 * @param {boolean[]} isActive
 * @return {string[]}
 */
var validateCoupons = function (code, businessLine, isActive) {
  let electronicsList = [],
    groceryList = [],
    pharmacyList = [],
    restaurantList = [];

  for (let i = 0; i < code.length; ++i) {
    if (!isActive[i]) continue;

    const regexObj = /^[a-zA-Z0-9_]+$/i;
    if (!regexObj.test(code[i])) continue;

    if (businessLine[i] == "electronics") {
      electronicsList.push(code[i]);
    } else if (businessLine[i] == "grocery") {
      groceryList.push(code[i]);
    } else if (businessLine[i] == "pharmacy") {
      pharmacyList.push(code[i]);
    } else if (businessLine[i] == "restaurant") {
      restaurantList.push(code[i]);
    }
  }

  electronicsList.sort();
  groceryList.sort();
  pharmacyList.sort();
  restaurantList.sort();

  return [
    ...electronicsList,
    ...groceryList,
    ...pharmacyList,
    ...restaurantList,
  ];
};
