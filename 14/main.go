package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	x int
	y int
}

func (p *Point) add(other Point) Point {
	return Point{x: p.x + other.x, y: p.y + other.y}
}

type Segment struct {
	start Point
	end   Point
}

func (s *Segment) contains(v Point) bool {
	return min(s.start.x, s.end.x) <= v.x && v.x <= max(s.start.x, s.end.x) &&
		min(s.start.y, s.end.y) <= v.y && v.y <= max(s.start.y, s.end.y)
}

func containsInCave(cave []Segment, p Point) bool {
	for _, seg := range cave {
		if seg.contains(p) {
			return true
		}
	}
	return false
}

func hitTheBottom(threshold int, bottom Point) bool {
	return bottom.y == threshold+2
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func parseV(line string) Point {
	coords := strings.Split(line, ",")

	x, err := strconv.Atoi(coords[0])
	if err != nil {
		panic(err)
	}
	y, err := strconv.Atoi(coords[1])
	if err != nil {
		panic(err)
	}
	return Point{x, y}
}

func maxOfY(cave []Segment) int {
	maxY := -1
	for _, v := range cave {
		maxY = max(maxY, v.start.y)
		maxY = max(maxY, v.end.y)
	}
	return maxY
}

func main() {
	dat, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	var cave []Segment
	for _, line := range strings.Split(string(dat), "\n") {
		line = strings.TrimRight(line, "\n")
		borders := strings.Split(line, " -> ")
		start := parseV(borders[0])
		for _, v := range borders[1:] {
			end := parseV(v)
			segment := Segment{start: start, end: end}
			cave = append(cave, segment)
			start = end
		}
	}

	sandSource := Point{x: 500, y: 0}
	threshold := maxOfY(cave)
	fmt.Printf("part 1 = %d\n", part1(cave, sandSource, threshold))
	fmt.Printf("part 2 = %d\n", part2(cave, sandSource, threshold))
}

func part1(cave []Segment, sandSource Point, threshold int) int {
	sand := make(map[Point]struct{})

	for {
		newGrain := sandSource
		for {
			if newGrain.y > threshold {
				break
			}

			bottom := newGrain.add(Point{0, 1})
			_, ok := sand[bottom]
			if !containsInCave(cave, bottom) && !ok {
				newGrain = bottom
				continue
			}

			bottomLeft := newGrain.add(Point{-1, 1})
			_, ok = sand[bottomLeft]
			if !containsInCave(cave, bottomLeft) && !ok {
				newGrain = bottomLeft
				continue
			}

			bottomRight := newGrain.add(Point{1, 1})
			_, ok = sand[bottomRight]
			if !containsInCave(cave, bottomRight) && !ok {
				newGrain = bottomRight
				continue
			}
			break
		}
		if threshold < newGrain.y {
			break
		}
		sand[newGrain] = struct{}{}
	}
	return len(sand)
}

func part2(cave []Segment, sandSource Point, threshold int) int {
	sand := make(map[Point]struct{})

	for {
		newGrain := sandSource
		for {
			bottom := newGrain.add(Point{0, 1})
			_, ok := sand[bottom]
			if !containsInCave(cave, bottom) && !ok && !hitTheBottom(threshold, bottom) {
				newGrain = bottom
				continue
			}
			bottomLeft := newGrain.add(Point{-1, 1})
			_, ok = sand[bottomLeft]
			if !containsInCave(cave, bottomLeft) && !ok && !hitTheBottom(threshold, bottomLeft) {
				newGrain = bottomLeft
				continue
			}
			bottomRight := newGrain.add(Point{1, 1})
			_, ok = sand[bottomRight]
			if !containsInCave(cave, bottomRight) && !ok && !hitTheBottom(threshold, bottomRight) {
				newGrain = bottomRight
				continue
			}
			break
		}
		sand[newGrain] = struct{}{}
		if newGrain.x == sandSource.x && newGrain.y == sandSource.y {
			break
		}
	}
	return len(sand)
}
