## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-559.0.0.0.0
-  __TEXT.__text: 0x125a7c
-  __TEXT.__auth_stubs: 0x1be0
+564.0.0.0.0
+  __TEXT.__text: 0x132e30
+  __TEXT.__auth_stubs: 0x1c20
   __TEXT.__objc_stubs: 0x1f20
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__gcc_except_tab: 0x12eb4
-  __TEXT.__const: 0xa924
-  __TEXT.__cstring: 0x14fb9
-  __TEXT.__oslogstring: 0x19781
-  __TEXT.__objc_methname: 0x1b34
+  __TEXT.__cstring: 0x15d79
+  __TEXT.__const: 0xa12c
+  __TEXT.__gcc_except_tab: 0x15ddc
+  __TEXT.__oslogstring: 0x19b29
   __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methtype: 0x8c5
-  __TEXT.__swift5_typeref: 0x36
+  __TEXT.__objc_methname: 0x1b34
   __TEXT.__constg_swiftt: 0xd4
-  __TEXT.__swift5_reflstr: 0xb
-  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__swift5_typeref: 0x36
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x7640
-  __TEXT.__eh_frame: 0x398
-  __DATA_CONST.__const: 0xaa18
+  __TEXT.__swift5_reflstr: 0xb
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__unwind_info: 0x7e30
+  __TEXT.__eh_frame: 0x3b0
+  __DATA_CONST.__const: 0xaa78
   __DATA_CONST.__cfstring: 0xc80
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xe10
-  __DATA_CONST.__got: 0x550
-  __DATA_CONST.__auth_ptr: 0x48
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__auth_got: 0xe30
+  __DATA_CONST.__got: 0x560
+  __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x850
   __DATA.__objc_selrefs: 0x940
   __DATA.__objc_ivar: 0x48

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5799
-  Symbols:   665
-  CStrings:  3608
+  Functions: 6098
+  Symbols:   671
+  CStrings:  3709
 
Symbols:
+ __ZTISt18bad_variant_access
+ __ZTVSt18bad_variant_access
+ _malloc_good_size
+ _malloc_type_malloc
+ _malloc_type_realloc
+ _strpbrk
CStrings:
+ "\n      INSERT INTO sessions_new (session_id, state, start, end, params, cadence)\n      SELECT \n        CASE agg_session_period \n          WHEN 0 THEN 'com.apple.CoreAnalytics.Daily'\n          WHEN 1 THEN 'com.apple.CoreAnalytics.Weekly' \n          WHEN 2 THEN 'com.apple.CoreAnalytics.Monthly'\n          WHEN 3 THEN 'com.apple.CoreAnalytics.Quarterly'\n        END as session_id,\n        1 as state,\n        strftime('%s', agg_session_start_timestamp) * 1000000 as start,\n        strftime('%s', agg_session_end_boundary) * 1000000 as end,\n        NULL as params,\n        agg_session_period as cadence\n      FROM (\n        SELECT agg_session_period, agg_session_start_timestamp, agg_session_end_boundary\n        FROM agg_session \n        WHERE agg_session_period IN (0, 1, 2, 3)\n        GROUP BY agg_session_period\n        HAVING agg_session_id = MIN(agg_session_id)\n      ) distinct_sessions\n    "
+ "\n      UPDATE sessions SET end = end * 1000000 WHERE end > 0 AND end < 1000000000000;\n    "
+ "\n      UPDATE sessions SET start = start * 1000000 WHERE start > 0 AND start < 1000000000000;\n    "
+ ":!="
+ ":*"
+ ":+"
+ ":-"
+ ":/"
+ ":<"
+ ":<="
+ ":=="
+ ":>"
+ ":>="
+ ":abs"
+ ":and"
+ ":drop"
+ ":dropN"
+ ":dup"
+ ":dupN"
+ ":filter"
+ ":fold"
+ ":getSize"
+ ":hasKey"
+ ":if"
+ ":ifElse"
+ ":map"
+ ":max"
+ ":min"
+ ":not"
+ ":or"
+ ":pick"
+ ":pick2"
+ ":return"
+ ":roll"
+ ":rot"
+ ":sigdig"
+ ":swap"
+ ":xor"
+ "CREATE INDEX IF NOT EXISTS IX_modify_eventdefs_modify_event_name ON modify_eventdefs(modify_event_name); CREATE INDEX IF NOT EXISTS IX_config_modify_eventdefs_modify_eventdef_id ON config_modify_eventdefs(modify_eventdef_id);"
+ "CowSequence.h"
+ "Custom"
+ "EmbeddedArray.h"
+ "XPC dictionary key is not valid UTF-8"
+ "XPC string value is not valid UTF-8"
+ "[Config Store] DATABASE INITIALIZATION: modifying for V12 schema - restoring modify-event lookup indices dropped in V9"
+ "[Config Store] ERROR: Failed to restore modify-eventdef lookup indices; %s"
+ "[Config Store] ERROR: Failed to restore modify-eventdef lookup indices[null database]"
+ "[MotionStateResolver] WARNING: Failed to get any CoreMotion classes for activity"
+ "[MotionStateResolver] WARNING: Operation queue instance not found for motion."
+ "[State Store] DATABASE INITIALIZATION: modifying for V16 schema - repairing sessions.start/end rows that V13 migration stored in seconds instead of microseconds"
+ "[State Store] Failed to repair sessions.end values from seconds to microseconds; %s"
+ "[State Store] Failed to repair sessions.end values from seconds to microseconds[null database]"
+ "[State Store] Failed to repair sessions.start values from seconds to microseconds; %s"
+ "[State Store] Failed to repair sessions.start values from seconds to microseconds[null database]"
+ "[State Store] V16 repair: rewrote %d sessions.start row(s) and %d sessions.end row(s) from seconds to microseconds"
+ "\\\""
+ "\\\\"
+ "\\b"
+ "\\f"
+ "\\n"
+ "\\r"
+ "\\t"
+ "^$\\.*+?()[]{}|"
+ "contiguous_begin"
+ "copy_impl"
+ "decref"
+ "empty number"
+ "expected '"
+ "expected ',' or ']' in array"
+ "expected ',' or '}' in object"
+ "expected string key in object"
+ "incref"
+ "invalid UTF-8 code point"
+ "invalid UTF-8 continuation byte"
+ "invalid UTF-8 lead byte"
+ "invalid escape character: \\"
+ "invalid exponent"
+ "invalid floating-point number"
+ "invalid fractional part"
+ "invalid hex digit in \\uXXXX escape"
+ "invalid low surrogate"
+ "invalid number"
+ "invalid token (expected 'false')"
+ "invalid token (expected 'null')"
+ "invalid token (expected 'true')"
+ "lone high surrogate without low surrogate"
+ "lone low surrogate"
+ "m_size > 0"
+ "number too long"
+ "overlong UTF-8 sequence"
+ "pop_back"
+ "push_back"
+ "set_size"
+ "size"
+ "span"
+ "trailing content after JSON value"
+ "truncated UTF-8 sequence"
+ "truncated \\uXXXX escape"
+ "truncated escape sequence"
+ "unescaped control character in string"
+ "unexpected character: "
+ "unexpected end of input"
+ "unterminated array"
+ "unterminated object"
+ "unterminated string"
+ "{JsonValue={variant<std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>={__impl<std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=(__union<std::__variant_detail::_Trait::_Available, 0UL, std::monostate, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<0UL, std::monostate>={monostate=}}(__union<std::__variant_detail::_Trait::_Available, 1UL, JsonObject, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<1UL, JsonObject>={JsonObject={IntrusivePtr<apple::cow::detail::EmbeddedArray<JsonObjectPayloadHeader, JsonValue>>=^v}}}(__union<std::__variant_detail::_Trait::_Available, 2UL, JsonArray, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<2UL, JsonArray>={JsonArray={CowVector<JsonValue, 0U>={CowSequence<JsonValue, 0U>=(?=^{JsonValue}^v)[0C]Q}}}}(__union<std::__variant_detail::_Trait::_Available, 3UL, apple::cow::detail::CowString, bool, long long, unsigned long long, double>=c{__alt<3UL, apple::cow::detail::CowString>={CowString={CowSequence<char, 0U>=(?=*^v)[0C]Q}}}(__union<std::__variant_detail::_Trait::_Available, 4UL, bool, long long, unsigned long long, double>=c{__alt<4UL, bool>=B}(__union<std::__variant_detail::_Trait::_Available, 5UL, long long, unsigned long long, double>=c{__alt<5UL, long long>=q}(__union<std::__variant_detail::_Trait::_Available, 6UL, unsigned long long, double>=c{__alt<6UL, unsigned long long>=Q}(__union<std::__variant_detail::_Trait::_Available, 7UL, double>=c{__alt<7UL, double>=d}(__union<std::__variant_detail::_Trait::_Available, 8UL>=)))))))))I}}}8@?0"
+ "{vector<apple::cow::detail::CowString, std::allocator<apple::cow::detail::CowString>>=^{CowString}^{CowString}{?=^{CowString}}}8@?0"
- "\n      INSERT INTO sessions_new (session_id, state, start, end, params, cadence)\n      SELECT \n        CASE agg_session_period \n          WHEN 0 THEN 'com.apple.CoreAnalytics.Daily'\n          WHEN 1 THEN 'com.apple.CoreAnalytics.Weekly' \n          WHEN 2 THEN 'com.apple.CoreAnalytics.Monthly'\n          WHEN 3 THEN 'com.apple.CoreAnalytics.Quarterly'\n        END as session_id,\n        1 as state,\n        strftime('%s', agg_session_start_timestamp) as start,\n        strftime('%s', agg_session_end_boundary) as end,\n        NULL as params,\n        agg_session_period as cadence\n      FROM (\n        SELECT agg_session_period, agg_session_start_timestamp, agg_session_end_boundary\n        FROM agg_session \n        WHERE agg_session_period IN (0, 1, 2, 3)\n        GROUP BY agg_session_period\n        HAVING agg_session_id = MIN(agg_session_id)\n      ) distinct_sessions\n    "
- "[MotionStateResolver] WARNING: Failed to get any CoreMotion classes"
- "[MotionStateResolver] WARNING: Operation queue instance not found."
- "cannot use offsets with object iterators"
- "operator-"
- "operator--"
```
