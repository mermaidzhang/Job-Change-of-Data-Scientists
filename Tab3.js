let train = [
  { Score Type: "precision", accuracy : 0.762839, macro avg : 0.671710,weighted avg : 0.738732,model: "RandomForest" },
  { Score Type: "recall", accuracy : 0.762839, macro avg : 0.622749,weighted avg : 0.762839,model: "RandomForest" },
  { Score Type: "f1-score", accuracy : 0.762839, macro avg : 	0.635110,weighted avg : 0.743369,model: "RandomForest" },
  { Score Type: "precision", accuracy : 0.715866, macro avg : 0.590508,weighted avg : 0.686525,model: "KNN" },
  { Score Type: "recall", accuracy : 0.715866	, macro avg : 0.569086,weighted avg : 0.715866,model: "KNN" },
  { Score Type: "f1-score", accuracy : 0.715866	, macro avg : 0.573260,weighted avg : 0.696966,model: "KNN" },
  { Score Type: "precision", accuracy : 0.673486, macro avg : 0.616122,weighted avg : 0.726707,model: "LogisticRegression" },
  { Score Type: "f1-score", accuracy : 0.673486, macro avg : 0.644636	,weighted avg : 0.673486,model: "LogisticRegression" },
  { Score Type: "recall", accuracy : 0.673486, macro avg : 0.618111,weighted avg : 0.673486,model: "LogisticRegression" }
];



function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for (let key of data) {
    let th = document.createElement("th");
    let text = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  }
}
  
function generateTable(table, data) {
  for (let element of data) {
    let row = table.insertRow();
    for (key in element) {
      let cell = row.insertCell();
      let text = document.createTextNode(element[key]);
      cell.appendChild(text);
    }
  }
}
  
let table = document.querySelector("table");
let data = Object.keys(train[0]);
generateTable(table, train);
generateTableHead(table, data);

  