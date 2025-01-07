## libANGLE-shared.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib`

```diff

-620.2.2.0.0
+620.2.3.0.0
   __TEXT.__text: 0x2674b4
   __TEXT.__auth_stubs: 0xe10
   __TEXT.__const: 0x87db0
-  __TEXT.__cstring: 0x47e18
+  __TEXT.__cstring: 0x47e23
   __TEXT.__gcc_except_tab: 0x2e60
   __TEXT.__oslogstring: 0xf
   __TEXT.__unwind_info: 0x1968
CStrings:
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ilshift(X x, Y y)\n{\n    return as_type<X>(metal::select(metal::make_unsigned_t<X>(0), metal::make_unsigned_t<X>(x) << (y & Y(31)), metal::make_unsigned_t<Y>(y) < metal::make_unsigned_t<Y>(32)));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_rshift(X x, Y y)\n{\n    return metal::select(X(0), x >> (y & Y(31)), metal::make_unsigned_t<Y>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"
+ "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ulshift(X x, Y y)\n{\n    return metal::select(X(0), x << (y & Y(31)), metal::make_unsigned_t<Y>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"
+ "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_div(X x, Y y)\n{\n    Z zx = Z(x);\n    Z zy = Z(y);\n    auto predicate = zy == Z(0);\n    return zx / metal::select(zy, Z(1), predicate);\n}\n\n"
+ "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_iadd(X x, Y y)\n{\n    return as_type<Z>(metal::make_unsigned_t<Z>(x) + metal::make_unsigned_t<Z>(y));\n}\n\n"
+ "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_imod(X x, Y y)\n{\n    if constexpr (metal::is_signed_v<Z>) {\n        Z y_or_one = metal::select(Z(y), Z(1), Z(y) == Z(0));\n        if (metal::any(((Z(x) | y_or_one) & Z(2147483648u)) != Z(0u)))\n        {\n            return as_type<Z>(\n                metal::make_unsigned_t<Z>(x) - metal::make_unsigned_t<Z>(x / y_or_one) * metal::make_unsigned_t<Z>(y_or_one)\n            );\n        }\n        else\n        {\n            return x % y_or_one;\n        }\n    }\n    else\n    {\n        return x % metal::select(Z(y), Z(1u), Z(y) == Z(0u));\n    }\n}\n\n"
+ "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_imul(X x, Y y)\n{\n    return as_type<Z>(metal::make_unsigned_t<Z>(x) * metal::make_unsigned_t<Z>(y));\n}\n\n"
+ "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_isub(X x, Y y)\n{\n    return as_type<Z>(metal::make_unsigned_t<Z>(x) - metal::make_unsigned_t<Z>(y));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_div(X x, Y y)\n{\n    auto predicate = X(y) == X(0);\n    if constexpr (metal::is_signed_v<X>)\n    {\n        predicate = predicate || (x == X(metal::numeric_limits<X>::lowest()) && X(y) == X(-1));\n    }\n    return x / metal::select(X(y), X(1), predicate);\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_iadd(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) + as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ilshift(X x, Y y)\n{\n    return as_type<X>(metal::select(metal::make_unsigned_t<X>(0), as_type<metal::make_unsigned_t<X>>(x) << (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32)));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_imod(X x, Y y)\n{\n    if constexpr (metal::is_signed_v<X>) {\n        X y_or_one = metal::select(X(y), X(1), ((X(y) == X(0)) | ((x == X(metal::numeric_limits<X>::lowest())) & (X(y) == X(-1)))));\n        if (metal::any((X(x | y_or_one) & X(2147483648u)) != X(0u)))\n        {\n            return as_type<X>(\n                as_type<metal::make_unsigned_t<X>>(x) - as_type<metal::make_unsigned_t<X>>(x / y_or_one) * as_type<metal::make_unsigned_t<X>>(y_or_one)\n            );\n        }\n        else\n        {\n            return x % y_or_one;\n        }\n    }\n    else\n    {\n        return x % metal::select(X(y), X(1u), X(y) == X(0u));\n    }\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_imul(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) * as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_isub(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) - as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_rshift(X x, Y y)\n{\n    return metal::select(X(0), x >> (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ulshift(X x, Y y)\n{\n    return metal::select(X(0), x << (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"

```
