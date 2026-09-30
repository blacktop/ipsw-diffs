## MapsSuggestions

> `/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions`

```diff

-2859.30.7.3.5
-  __TEXT.__text: 0x13af64
-  __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0x6820
+2864.31.7.31.2
+  __TEXT.__text: 0x13c948
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_methlist: 0x6840
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0x273ae
-  __TEXT.__oslogstring: 0x1320f
-  __TEXT.__swift5_typeref: 0x851
+  __TEXT.__cstring: 0x27453
+  __TEXT.__oslogstring: 0x13278
+  __TEXT.__swift5_typeref: 0x84f
   __TEXT.__constg_swiftt: 0x66c
   __TEXT.__swift5_reflstr: 0x3f4
   __TEXT.__swift5_fieldmd: 0x438
-  __TEXT.__swift5_capture: 0x5a8
+  __TEXT.__swift5_capture: 0x6c0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x135d4
+  __TEXT.__gcc_except_tab: 0x137e4
   __TEXT.__ustring: 0x1b2
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x50e8
-  __TEXT.__eh_frame: 0xb48
+  __TEXT.__unwind_info: 0x5140
+  __TEXT.__eh_frame: 0xb38
   __TEXT.__objc_classname: 0x24ec
-  __TEXT.__objc_methname: 0x10e79
-  __TEXT.__objc_methtype: 0x61ca
-  __TEXT.__objc_stubs: 0xa960
-  __DATA_CONST.__got: 0xe58
-  __DATA_CONST.__const: 0xba98
+  __TEXT.__objc_methname: 0x10f08
+  __TEXT.__objc_methtype: 0x61e2
+  __TEXT.__objc_stubs: 0xa9a0
+  __DATA_CONST.__got: 0xe50
+  __DATA_CONST.__const: 0xbb70
   __DATA_CONST.__objc_classlist: 0x6d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3620
+  __DATA_CONST.__objc_selrefs: 0x3640
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH_CONST.__auth_got: 0xc30
   __AUTH_CONST.__auth_ptr: 0xd8
-  __AUTH_CONST.__const: 0x72e8
+  __AUTH_CONST.__const: 0x7538
   __AUTH_CONST.__cfstring: 0xcf40
-  __AUTH_CONST.__objc_const: 0x18be8
+  __AUTH_CONST.__objc_const: 0x18c18
   __AUTH_CONST.__objc_intobj: 0x720
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__objc_floatobj: 0xa0
   __AUTH.__objc_data: 0xd10
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x6e4
-  __DATA.__data: 0x4b00
+  __DATA.__objc_ivar: 0x6e8
+  __DATA.__data: 0x4b60
   __DATA.__common: 0x48
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_ivar: 0x1a4
   __DATA_DIRTY.__objc_data: 0x4440
-  __DATA_DIRTY.__data: 0x358
+  __DATA_DIRTY.__data: 0x388
   __DATA_DIRTY.__common: 0xb0
   __DATA_DIRTY.__bss: 0x858
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4681
-  Symbols:   5566
-  CStrings:  8899
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4704
+  Symbols:   5586
+  CStrings:  8910
 
Symbols:
+ _IsEVRoutingSupported
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x11\x16"
+ "-[MapsSuggestionsETARequester setAutomobileOptions:]_block_invoke"
+ "-[MapsSuggestionsRoutine fetchAllSuggestedLOIsExcludingTypes:minVisits:maxAge:maxResults:handler:]_block_invoke"
+ "-[MapsSuggestionsRoutine fetchSuggestedLOIsForTypes:minVisits:maxAge:maxResults:handler:]"
+ "-[MapsSuggestionsRoutine fetchSuggestedLOIsForTypes:minVisits:maxAge:maxResults:handler:]_block_invoke"
+ "18:48:34"
+ "Aug  3 2024"
+ "No types give to fetch. Not attempting to fetch shortcuts"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSDate\",C,N,V_mapsSyncCreateTime"
+ "_mapsSyncCreateTime"
+ "_suppressionEntries is not a NSDictionary:<%!p(MISSING)>"
+ "c56@0:8@16Q24d32Q40@?48"
+ "fetchAllSuggestedLOIsExcludingTypes:minVisits:maxAge:maxResults:handler:"
+ "fetchSuggestedLOIsForTypes:minVisits:maxAge:maxResults:handler:"
+ "mapsSyncCreateTime"
+ "q24@?0@\"RTLocationOfInterest\"8@\"RTLocationOfInterest\"16"
+ "setMapsSyncCreateTime:"
+ "stringContacts"
+ "subarrayWithRange:"
- "\x11\x15"
- "-[MapsSuggestionsRoutine fetchSuggestedLOIsForType:minVisits:maxAge:handler:]"
- "-[MapsSuggestionsRoutine fetchSuggestedLOIsForType:minVisits:maxAge:handler:]_block_invoke"
- "-[MapsSuggestionsRoutine fetchSuggestedLOIsForType:minVisits:maxAge:handler:]_block_invoke_2"
- "00:14:32"
- "Jul 17 2024"
- "T@\"GEOAutomobileOptions\",&,V_automobileOptions"
- "currentCountrySupportsElectricVehicleRouting"
- "fetchSuggestedLOIsForType:minVisits:maxAge:handler:"

```
