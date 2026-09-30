## libANGLE-shared.dylib

> `/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib`

```diff

-624.4.5.11.5
-  __TEXT.__text: 0x25aa68
+624.5.1.11.2
+  __TEXT.__text: 0x25ad3c
   __TEXT.__auth_stubs: 0xd00
-  __TEXT.__const: 0x84000
-  __TEXT.__cstring: 0x444c6
+  __TEXT.__const: 0x84040
+  __TEXT.__cstring: 0x44733
   __TEXT.__gcc_except_tab: 0x2c94
   __TEXT.__oslogstring: 0xf
   __TEXT.__unwind_info: 0x17a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9000
-  Symbols:   13357
-  CStrings:  7251
+  Functions: 9001
+  Symbols:   13358
+  CStrings:  7254
 
Symbols:
+ __ZN12_GLOBAL__N_114ProgramPrelude9negateIntEv
+ __ZN2gl33ValidateDrawElementsInstancedBaseEPKNS_7ContextEN5angle10EntryPointENS_13PrimitiveModeEiNS_16DrawElementsTypeEPKviij
- __ZN2gl33ValidateDrawElementsInstancedBaseEPKNS_7ContextEN5angle10EntryPointENS_13PrimitiveModeEiNS_16DrawElementsTypeEPKvij
CStrings:
+ "\ntemplate <typename T>\nANGLE_ALWAYS_INLINE T ANGLE_negateInt(T x)\n{\n    return as_type<T>(metal::make_unsigned_t<T>(0) - metal::make_unsigned_t<T>(x));\n}\n\n"
+ "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_div(X x, Y y)\n{\n    Z zx = Z(x);\n    Z zy = Z(y);\n    if constexpr (metal::is_signed_v<Z>) {\n        using U = metal::make_unsigned_t<Z>;\n        Z safeY = metal::select(zy, Z(1), zy == Z(0));\n        auto isNegOne = safeY == Z(-1);\n        safeY = metal::select(safeY, Z(1), isNegOne);\n        Z q = zx / safeY;\n        return metal::select(q, as_type<Z>(U(0) - U(zx)), isNegOne);\n    } else {\n        return zx / metal::select(zy, Z(1), zy == Z(0));\n    }\n}\n\n"
+ "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_imod(X x, Y y)\n{\n    if constexpr (metal::is_signed_v<Z>) {\n        Z y_or_one = metal::select(Z(y), Z(1), Z(y) == Z(0));\n        y_or_one = metal::select(y_or_one, Z(1), y_or_one == Z(-1));\n        if (metal::any(((Z(x) | y_or_one) & Z(2147483648u)) != Z(0u)))\n        {\n            return as_type<Z>(\n                metal::make_unsigned_t<Z>(x) - metal::make_unsigned_t<Z>(x / y_or_one) * metal::make_unsigned_t<Z>(y_or_one)\n            );\n        }\n        else\n        {\n            return x % y_or_one;\n        }\n    }\n    else\n    {\n        return x % metal::select(Z(y), Z(1u), Z(y) == Z(0u));\n    }\n}\n\n"
+ "ANGLE_negateInt"
+ "Effective vertex index (index + basevertex) is negative."
- "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_div(X x, Y y)\n{\n    Z zx = Z(x);\n    Z zy = Z(y);\n    auto predicate = zy == Z(0);\n    return zx / metal::select(zy, Z(1), predicate);\n}\n\n"
- "\ntemplate<typename X, typename Y, typename Z = metal::conditional_t<metal::is_scalar_v<Y>, X, Y>>\nANGLE_ALWAYS_INLINE Z ANGLE_imod(X x, Y y)\n{\n    if constexpr (metal::is_signed_v<Z>) {\n        Z y_or_one = metal::select(Z(y), Z(1), Z(y) == Z(0));\n        if (metal::any(((Z(x) | y_or_one) & Z(2147483648u)) != Z(0u)))\n        {\n            return as_type<Z>(\n                metal::make_unsigned_t<Z>(x) - metal::make_unsigned_t<Z>(x / y_or_one) * metal::make_unsigned_t<Z>(y_or_one)\n            );\n        }\n        else\n        {\n            return x % y_or_one;\n        }\n    }\n    else\n    {\n        return x % metal::select(Z(y), Z(1u), Z(y) == Z(0u));\n    }\n}\n\n"
```
