; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"print"(i32 %".1")

define i32 @"fibonacci"(i32 %"n")
{
alloca-zqdqjeds:
  %"n.1" = alloca i32
  %"check" = alloca i32
  %"res" = alloca i1
  %"minus_1" = alloca i32
  %"n_minus_1" = alloca i32
  %"fib_1" = alloca i32
  %"minus_2" = alloca i32
  %"n_minus_2" = alloca i32
  %"fib_2" = alloca i32
  %"fib_sum" = alloca i32
  br label %"entry-lxsxxuhe"
entry-lxsxxuhe:
  store i32 %"n", i32* %"n.1"
  store i32 2, i32* %"check"
  %".5" = load i32, i32* %"n.1"
  %".6" = load i32, i32* %"check"
  %"res.1" = icmp slt i32 %".5", %".6"
  store i1 %"res.1", i1* %"res"
  %".8" = load i1, i1* %"res"
  br i1 %".8", label %"l_true", label %"l_false"
l_true:
  %".10" = load i32, i32* %"n.1"
  ret i32 %".10"
l_false:
  store i32 -1, i32* %"minus_1"
  %".13" = load i32, i32* %"n.1"
  %".14" = load i32, i32* %"minus_1"
  %"n_minus_1.1" = add i32 %".13", %".14"
  store i32 %"n_minus_1.1", i32* %"n_minus_1"
  %".16" = load i32, i32* %"n_minus_1"
  %"fib_1.1" = call i32 @"fibonacci"(i32 %".16")
  store i32 %"fib_1.1", i32* %"fib_1"
  store i32 -2, i32* %"minus_2"
  %".19" = load i32, i32* %"n.1"
  %".20" = load i32, i32* %"minus_2"
  %"n_minus_2.1" = add i32 %".19", %".20"
  store i32 %"n_minus_2.1", i32* %"n_minus_2"
  %".22" = load i32, i32* %"n_minus_2"
  %"fib_2.1" = call i32 @"fibonacci"(i32 %".22")
  store i32 %"fib_2.1", i32* %"fib_2"
  %".24" = load i32, i32* %"fib_1"
  %".25" = load i32, i32* %"fib_2"
  %"fib_sum.1" = add i32 %".24", %".25"
  store i32 %"fib_sum.1", i32* %"fib_sum"
  %".27" = load i32, i32* %"fib_sum"
  ret i32 %".27"
}

define void @"main"()
{
alloca-pjsffiwr:
  %"n" = alloca i32
  %"tmp" = alloca i32
  %"temp" = alloca i32
  br label %"entry-lxmuyngx"
entry-lxmuyngx:
  store i32 6, i32* %"n"
  %".3" = load i32, i32* %"n"
  %"tmp.1" = call i32 @"fibonacci"(i32 %".3")
  store i32 %"tmp.1", i32* %"tmp"
  %".5" = load i32, i32* %"tmp"
  %"temp.1" = call i32 @"print"(i32 %".5")
  store i32 %"temp.1", i32* %"temp"
  ret void
}

