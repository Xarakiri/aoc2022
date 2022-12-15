package main

import "testing"

func TestContains(t *testing.T) {
	seg := Segment{start: Point{10, 20}, end: Point{30, 50}}
	val := Point{20, 40}

	if !seg.contains(val) {
		t.Error("contains don`t work")
	}
}

func TestAdd(t *testing.T) {
	first := Point{10, 20}
	second := Point{30, 50}
	val := first.add(second)
	if val.x != 40 && val.y != 70 {
		t.Error("add error")
	}
}
