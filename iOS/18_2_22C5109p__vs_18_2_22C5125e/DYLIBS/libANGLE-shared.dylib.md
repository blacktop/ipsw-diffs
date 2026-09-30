## libANGLE-shared.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib`

```diff

-620.1.11.10.8
-  __TEXT.__text: 0x266f94
+620.1.14.10.4
+  __TEXT.__text: 0x2675a8
   __TEXT.__auth_stubs: 0xe10
   __TEXT.__const: 0x87db0
-  __TEXT.__cstring: 0x474b4
+  __TEXT.__cstring: 0x47dfd
   __TEXT.__gcc_except_tab: 0x2e40
   __TEXT.__oslogstring: 0xf
   __TEXT.__unwind_info: 0x1960

   __AUTH_CONST.__const: 0x16b98
   __AUTH_CONST.__cfstring: 0x9e0
   __DATA.__data: 0x2ee18
-  __DATA.__common: 0x378
+  __DATA.__common: 0x370
   __DATA.__bss: 0x4
   __DATA_DIRTY.__data: 0xfd8
-  __DATA_DIRTY.__common: 0x4a0
+  __DATA_DIRTY.__common: 0x4a8
   __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9520
-  Symbols:   9893
-  CStrings:  8055
+  Functions: 9527
+  Symbols:   9900
+  CStrings:  8072
 
CStrings:
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_div(X x, Y y)\n{\n    auto predicate = X(y) == X(0);\n    if constexpr (metal::is_signed_v<X>)\n    {\n        predicate = predicate || (x == X(metal::numeric_limits<X>::lowest()) && X(y) == X(-1));\n    }\n    return x / metal::select(X(y), X(1), predicate);\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ftoi(Y y)\n{\n    auto min = metal::numeric_limits<X>::min();\n    auto max = metal::numeric_limits<X>::max();\n    return X(metal::clamp(y, Y(min), Y(max)));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_iadd(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) + as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ilshift(X x, Y y)\n{\n    return as_type<X>(metal::select(metal::make_unsigned_t<X>(0), as_type<metal::make_unsigned_t<X>>(x) << (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32)));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_imod(X x, Y y)\n{\n    if constexpr (metal::is_signed_v<X>) {\n        X y_or_one = metal::select(X(y), X(1), ((X(y) == X(0)) | ((x == X(metal::numeric_limits<X>::lowest())) & (X(y) == X(-1)))));\n        if (metal::any((X(x | y_or_one) & X(2147483648u)) != X(0u)))\n        {\n            return as_type<X>(\n                as_type<metal::make_unsigned_t<X>>(x) - as_type<metal::make_unsigned_t<X>>(x / y_or_one) * as_type<metal::make_unsigned_t<X>>(y_or_one)\n            );\n        }\n        else\n        {\n            return x %!y(MISSING)_or_one;\n        }\n    }\n    else\n    {\n        return x %!m(MISSING)etal::select(X(y), X(1u), X(y) == X(0u));\n    }\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_imul(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) * as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_isub(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) - as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_rshift(X x, Y y)\n{\n    return metal::select(X(0), x >> (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ulshift(X x, Y y)\n{\n    return metal::select(X(0), x << (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"
+ "ANGLE_div"
+ "ANGLE_ftoi<"
+ "ANGLE_iadd"
+ "ANGLE_ilshift"
+ "ANGLE_imod"
+ "ANGLE_imul"
+ "ANGLE_isub"
+ "ANGLE_rshift"
+ "ANGLE_ulshift"
- "\ntemplate <typename T, int Cols, int Rows>\nANGLE_ALWAYS_INLINE thread metal::matrix<T, Cols, Rows> &operator/=(thread metal::matrix<T, Cols, Rows> &a, metal::matrix<T, Cols, Rows> b)\n{\n    a = a / b;\n    return a;\n}\n\n"

```
