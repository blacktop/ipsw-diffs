## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-427.0.40.0.0
-  __TEXT.__text: 0x4f59c
+427.0.44.0.0
+  __TEXT.__text: 0x4f7cc
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0xd160
-  __TEXT.__objc_methlist: 0x615c
+  __TEXT.__objc_stubs: 0xd1a0
+  __TEXT.__objc_methlist: 0x6164
   __TEXT.__const: 0x210
-  __TEXT.__gcc_except_tab: 0xbc8
-  __TEXT.__oslogstring: 0x4d63
-  __TEXT.__objc_methname: 0x10d4d
+  __TEXT.__gcc_except_tab: 0xbe0
+  __TEXT.__oslogstring: 0x4d55
+  __TEXT.__objc_methname: 0x10d4e
   __TEXT.__cstring: 0x2c20
   __TEXT.__objc_classname: 0x13c8
-  __TEXT.__objc_methtype: 0x303d
+  __TEXT.__objc_methtype: 0x306a
   __TEXT.__swift5_typeref: 0x74
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_reflstr: 0x10
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x14d0
-  __DATA_CONST.__const: 0x1980
+  __TEXT.__unwind_info: 0x14e0
+  __DATA_CONST.__const: 0x1978
   __DATA_CONST.__cfstring: 0x2680
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xccf0
-  __DATA.__objc_selrefs: 0x3b20
+  __DATA.__objc_selrefs: 0x3b38
   __DATA.__objc_ivar: 0x5d4
   __DATA.__objc_data: 0x2ff0
   __DATA.__data: 0x1750

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1883
-  Symbols:   445
-  CStrings:  3918
+  Functions: 1885
+  Symbols:   446
+  CStrings:  3921
 
Symbols:
+ _OBJC_CLASS_$_UNNotificationIcon
CStrings:
+ "@\"SHPreRecordingRequest\""
+ "Fetching media item from data store for mediaItem ID: %@"
+ "No data store to retrieve media item."
+ "T@\"SHPreRecordingRequest\",R,N,V_request"
+ "fetchMediaItemForLibraryTrackIdentifier:"
+ "iconForApplicationIdentifier:"
+ "initWithRequest:audioTapProvider:"
+ "mediaItemForIdentifier:"
+ "mediaItemForIdentifier:completionHandler:"
+ "mediaItemValue"
+ "notificationIcon"
+ "prepareMatcherForRequest:completionHandler:"
+ "setIcon:"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"SHMediaItem\"@\"NSError\">24"
+ "v32@0:8@\"SHPreRecordingRequest\"16@?<v@?>24"
- "Fetching raw song response from data store for mediaItem ID: %@"
- "No data store to retrieve raw song response."
- "T@\"NSUUID\",R,N,V_requestID"
- "_requestID"
- "fetchRawSongResponseDataForLibraryTrackIdentifier:"
- "fetchRawSongResponseDataForMediaItemIdentifier:completionHandler:"
- "initWithRequestID:audioTapProvider:"
- "prepareMatcherForRequestID:completionHandler:"
- "rawSongResponseDataForMediaItemIdentifier:"
- "setResultType:"
- "v32@0:8@\"NSUUID\"16@?<v@?>24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"NSError\">24"
```
