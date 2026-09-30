## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3486.0.46.502.1
-  __TEXT.__text: 0x14ac44
+3486.0.81.502.4
+  __TEXT.__text: 0x14ae04
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x12d7c
+  __TEXT.__objc_methlist: 0x12d94
   __TEXT.__const: 0x5fe2
-  __TEXT.__cstring: 0xd078
+  __TEXT.__cstring: 0xd106
   __TEXT.__gcc_except_tab: 0x4a8c
   __TEXT.__oslogstring: 0xd5f
-  __TEXT.__unwind_info: 0x49b0
+  __TEXT.__unwind_info: 0x49b8
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x368
-  __DATA_CONST.__objc_selrefs: 0x5e98
+  __DATA_CONST.__objc_selrefs: 0x5ea0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x720
   __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0xf020
-  __AUTH_CONST.__objc_const: 0x16bf8
+  __AUTH_CONST.__cfstring: 0xf0a0
+  __AUTH_CONST.__objc_const: 0x16c28
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0x6e0
   __AUTH.__objc_data: 0x29e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1114
+  __DATA.__objc_ivar: 0x1118
   __DATA.__data: 0x521
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xb90

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7902
-  Symbols:   12934
-  CStrings:  2138
+  Functions: 7904
+  Symbols:   12938
+  CStrings:  2142
 
Symbols:
+ +[PPSSQLiteTimeSeriesIngester _stringForSourceNames:metrics:predicate:distinct:]
+ -[PPSTimeSeriesRequest initWithMetrics:predicate:timeFilter:limitCount:offsetCount:readDirection:returnsDistinctEntities:]
+ -[PPSTimeSeriesRequest returnsDistinctEntities]
+ _OBJC_IVAR_$_PPSTimeSeriesRequest._returnsDistinctEntities
+ ___block_descriptor_99_e8_32s40s48s56s64r72r80r88r_e39_B32?0"NSArray"8^{PPSSQLiteRow=}16^24ls32l8r64l8s40l8s48l8s56l8r72l8r80l8r88l8
+ _objc_msgSend$_stringForSourceNames:metrics:predicate:distinct:
+ _objc_msgSend$initWithMetrics:predicate:timeFilter:limitCount:offsetCount:readDirection:returnsDistinctEntities:
- +[PPSSQLiteTimeSeriesIngester _stringForSourceNames:metrics:predicate:]
- ___block_descriptor_98_e8_32s40s48s56s64r72r80r88r_e39_B32?0"NSArray"8^{PPSSQLiteRow=}16^24ls32l8r64l8s40l8s48l8s56l8r72l8r80l8r88l8
- _objc_msgSend$_stringForSourceNames:metrics:predicate:
CStrings:
+ "%@::%lu::%d"
+ "<%@: %p { type: %ld, metrics: %@, predicate: %@, timeFilter: %@ limitCount:%ld offsetCount:%ld readDirection: %ld distinct: %d }>"
+ "Distinct requests cannot select the timestamp metric."
+ "Distinct requests require at least one metric."
+ "returnsDistinct"
- "<%@: %p { type: %ld, metrics: %@, predicate: %@, timeFilter: %@ limitCount:%ld offsetCount:%ld readDirection: %ld }>"
```
