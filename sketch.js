
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  var grid = 3;
  for (var x = 0; x < width; x += width/grid) {
		for (var y = 0; y < height; y += height/grid) {
			stroke(0);
			strokeWeight(4);
			line(x, 0, x, height);
			line(0, y, width, y);
		}
	}
}
