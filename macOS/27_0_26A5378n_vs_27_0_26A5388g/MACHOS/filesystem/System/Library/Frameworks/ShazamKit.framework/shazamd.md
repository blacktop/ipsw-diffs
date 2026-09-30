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
-  __TEXT.__text: 0x54d4c
+427.0.44.0.0
+  __TEXT.__text: 0x54fa0
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_stubs: 0xcf20
-  __TEXT.__objc_methlist: 0x6114
+  __TEXT.__objc_stubs: 0xcf60
+  __TEXT.__objc_methlist: 0x611c
   __TEXT.__const: 0x238
   __TEXT.__cstring: 0x2b7d
-  __TEXT.__oslogstring: 0x4cd6
-  __TEXT.__gcc_except_tab: 0xaf0
-  __TEXT.__objc_methname: 0x10a44
+  __TEXT.__oslogstring: 0x4cc8
+  __TEXT.__gcc_except_tab: 0xb08
+  __TEXT.__objc_methname: 0x10a45
   __TEXT.__objc_classname: 0x13c8
-  __TEXT.__objc_methtype: 0x303d
+  __TEXT.__objc_methtype: 0x306a
   __TEXT.__swift5_typeref: 0x74
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_reflstr: 0x10
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x14e8
-  __DATA_CONST.__const: 0x1c10
+  __TEXT.__unwind_info: 0x1500
+  __DATA_CONST.__const: 0x1c08
   __DATA_CONST.__cfstring: 0x25e0
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__got: 0x8f0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xccf0
-  __DATA.__objc_selrefs: 0x3ad8
+  __DATA.__objc_selrefs: 0x3af0
   __DATA.__objc_ivar: 0x5d4
   __DATA.__objc_data: 0x2ff0
   __DATA.__data: 0x1750

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1923
-  Symbols:   429
-  CStrings:  3907
+  Functions: 1925
+  Symbols:   430
+  CStrings:  3910
 
Symbols:
+ _OBJC_CLASS_$_UNNotificationIcon
CStrings:
+ "@\"SHPreRecordingRequest\""
+ "Fetching media item from data store for mediaItem ID: %@"
+ "No data store to retrieve media item."
+ "T@\"SHPreRecordingRequest\",R,V_request"
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
- "T@\"NSUUID\",R,V_requestID"
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
