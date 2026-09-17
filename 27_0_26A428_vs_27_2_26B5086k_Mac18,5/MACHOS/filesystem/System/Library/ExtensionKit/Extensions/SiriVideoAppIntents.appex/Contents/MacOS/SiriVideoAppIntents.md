## SiriVideoAppIntents

> `/System/Library/ExtensionKit/Extensions/SiriVideoAppIntents.appex/Contents/MacOS/SiriVideoAppIntents`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`

```diff

-3600.28.7.0.0
-  __TEXT.__text: 0x168fc
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__swift5_typeref: 0x11be
-  __TEXT.__const: 0x3e6e
-  __TEXT.__swift5_reflstr: 0x8ff
-  __TEXT.__swift5_assocty: 0x6b8
-  __TEXT.__constg_swiftt: 0x4b4
-  __TEXT.__swift5_fieldmd: 0x758
-  __TEXT.__swift5_proto: 0x334
-  __TEXT.__swift5_types: 0x68
-  __TEXT.__swift_as_entry: 0x80
-  __TEXT.__swift_as_ret: 0x44
-  __TEXT.__swift_as_cont: 0x38
+3605.20.2.0.0
+  __TEXT.__text: 0x19040
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__swift5_typeref: 0x1258
+  __TEXT.__const: 0x3ffe
+  __TEXT.__swift5_reflstr: 0x913
+  __TEXT.__swift5_assocty: 0x6d8
+  __TEXT.__constg_swiftt: 0x4d0
+  __TEXT.__swift5_fieldmd: 0x78c
+  __TEXT.__swift5_proto: 0x340
+  __TEXT.__swift5_types: 0x6c
+  __TEXT.__swift_as_entry: 0x88
+  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__swift_as_cont: 0x3c
   __TEXT.__cstring: 0x174
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x94
-  __TEXT.__swift5_capture: 0x50
+  __TEXT.__swift5_capture: 0x60
   __TEXT.__objc_classname: 0x77
-  __TEXT.__oslogstring: 0x24e
+  __TEXT.__oslogstring: 0x48e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xc68
-  __TEXT.__eh_frame: 0x430
-  __DATA_CONST.__const: 0xfe0
+  __TEXT.__unwind_info: 0xcd8
+  __TEXT.__eh_frame: 0x470
+  __DATA_CONST.__const: 0x1048
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__auth_ptr: 0x658
+  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__auth_ptr: 0x678
   __DATA.__objc_const: 0x120
-  __DATA.__data: 0xb98
+  __DATA.__data: 0xbe0
   __DATA.__common: 0xd0
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CoreTransferable.framework/Versions/A/CoreTransferable

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 959
-  Symbols:   67
-  CStrings:  38
+  Functions: 990
+  Symbols:   69
+  CStrings:  46
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ _swift_retain_n
CStrings:
+ "FindContentIntentValueQuery produced %ld items from %ld search results"
+ "FindContentIntentValueQuery: added TV episode entity: %s"
+ "FindContentIntentValueQuery: added TV season entity: %s"
+ "FindContentIntentValueQuery: added TV show entity: %s"
+ "FindContentIntentValueQuery: added movie entity: %s"
+ "FindContentIntentValueQuery: added person entity: %s"
+ "FindContentIntentValueQuery: no privateSearchResult found in VideoSearch"
+ "FindContentIntentValueQuery: skipping cast/crew member '%s' with nil canonicalID"
+ "FindContentIntentValueQuery: skipping unknown content type"
+ "FindContentIntentValueQuery: skipping unsupported content type"
+ "person"
- "No privateSearchResult found in VideoSearch"
- "Skipping unknown content type"
- "Skipping unsupported content type"
```
