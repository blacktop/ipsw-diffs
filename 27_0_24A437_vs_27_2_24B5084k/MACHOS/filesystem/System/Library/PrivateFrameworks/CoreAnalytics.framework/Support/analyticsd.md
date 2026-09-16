## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-569.0.5.0.0
-  __TEXT.__text: 0x13fa84
+577.40.5.0.0
+  __TEXT.__text: 0x141734
   __TEXT.__auth_stubs: 0x1e60
   __TEXT.__objc_stubs: 0x2cc0
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0xb9c
-  __TEXT.__cstring: 0x160d5
-  __TEXT.__const: 0xa2a4
-  __TEXT.__gcc_except_tab: 0x176e4
-  __TEXT.__oslogstring: 0x1af29
+  __TEXT.__gcc_except_tab: 0x17794
+  __TEXT.__const: 0xa464
+  __TEXT.__cstring: 0x16215
+  __TEXT.__oslogstring: 0x1af99
+  __TEXT.__objc_methname: 0x2f83
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1879
-  __TEXT.__objc_methname: 0x2f83
-  __TEXT.__constg_swiftt: 0xd4
   __TEXT.__swift5_typeref: 0x36
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_fieldmd: 0x5c
-  __TEXT.__swift5_types: 0x14
+  __TEXT.__constg_swiftt: 0xd4
   __TEXT.__swift5_reflstr: 0xb
+  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x9c38
-  __TEXT.__eh_frame: 0x3c0
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__unwind_info: 0x9cf8
+  __TEXT.__eh_frame: 0x3a8
   __DATA_CONST.__const: 0xadc8
   __DATA_CONST.__cfstring: 0xd40
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__auth_got: 0xf50
   __DATA_CONST.__got: 0x638
-  __DATA_CONST.__auth_ptr: 0x50
+  __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0xf00
   __DATA.__objc_selrefs: 0xeb8
   __DATA.__objc_ivar: 0x90

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6354
+  Functions: 6410
   Symbols:   734
-  CStrings:  4131
+  CStrings:  4139
 
CStrings:
+ "LocationNotAuthorized"
+ "LocationServicesDisabled"
+ "MarketNA"
+ "[CD] Market: Location not authorized"
+ "[CD] Market: Location services disabled"
+ "[CD] Market: Market unknown: %s"
+ "[CD] Market: Reporting market: %{private}s"
+ "bluetoothStatus"
+ "locationAuthorizationStatus"
+ "locationServicesEnabled"
+ "{JsonValue={variant<std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>={__impl<std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=(__union<std::__variant_detail::_Trait::_Available, 0UL, std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<0UL, std::monostate>={monostate=}}(__union<std::__variant_detail::_Trait::_Available, 1UL, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<1UL, JsonObject>={JsonObject={JsonColumnBlock<apple::cow::detail::CowString>={IntrusivePtr<jsonvalue::detail::JsonColumnBlock<apple::cow::detail::CowString>::Node, jsonvalue::detail::JsonColumnBlock<apple::cow::detail::CowString>::NodeTraits>=^{Node}}Q}}}(__union<std::__variant_detail::_Trait::_Available, 2UL, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<2UL, JsonArray>={JsonArray={JsonColumnBlock<void>={IntrusivePtr<jsonvalue::detail::JsonColumnBlock<>::Node, jsonvalue::detail::JsonColumnBlock<>::NodeTraits>=^{Node}}Q}}}(__union<std::__variant_detail::_Trait::_Available, 3UL, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<3UL, apple::cow::detail::CowString>={CowString={CowSequence<char, 23U>=[24C]}}}(__union<std::__variant_detail::_Trait::_Available, 4UL, bool, long long, unsigned long long, double>=c{__alt<4UL, bool>=B}(__union<std::__variant_detail::_Trait::_Available, 5UL, long long, unsigned long long, double>=c{__alt<5UL, long long>=q}(__union<std::__variant_detail::_Trait::_Available, 6UL, unsigned long long, double>=c{__alt<6UL, unsigned long long>=Q}(__union<std::__variant_detail::_Trait::_Available, 7UL, double>=c{__alt<7UL, double>=d}(__union<std::__variant_detail::_Trait::_Available, 8UL>=)))))))))I}}}8@?0"
- "LocationFrameworkNotSupported"
- "[CD] Market: Location framework not supported"
- "{JsonValue={variant<std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>={__impl<std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=(__union<std::__variant_detail::_Trait::_Available, 0UL, std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<0UL, std::monostate>={monostate=}}(__union<std::__variant_detail::_Trait::_Available, 1UL, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<1UL, JsonObject>={JsonObject={IntrusivePtr<apple::cow::detail::EmbeddedArray<JsonObjectPayloadHeader, JsonValue>>=^v}}}(__union<std::__variant_detail::_Trait::_Available, 2UL, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<2UL, JsonArray>={JsonArray={CowVector<JsonValue, 0U>={CowSequence<JsonValue, 0U>=[16C]}}}}(__union<std::__variant_detail::_Trait::_Available, 3UL, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<3UL, apple::cow::detail::CowString>={CowString={CowSequence<char, 0U>=[16C]}}}(__union<std::__variant_detail::_Trait::_Available, 4UL, bool, long long, unsigned long long, double>=c{__alt<4UL, bool>=B}(__union<std::__variant_detail::_Trait::_Available, 5UL, long long, unsigned long long, double>=c{__alt<5UL, long long>=q}(__union<std::__variant_detail::_Trait::_Available, 6UL, unsigned long long, double>=c{__alt<6UL, unsigned long long>=Q}(__union<std::__variant_detail::_Trait::_Available, 7UL, double>=c{__alt<7UL, double>=d}(__union<std::__variant_detail::_Trait::_Available, 8UL>=)))))))))I}}}8@?0"
```
