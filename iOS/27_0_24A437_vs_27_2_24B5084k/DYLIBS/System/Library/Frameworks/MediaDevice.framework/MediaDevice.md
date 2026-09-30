## MediaDevice

> `/System/Library/Frameworks/MediaDevice.framework/MediaDevice`

```diff

-360.75.1.2.0
-  __TEXT.__text: 0x301fc
+385.6.1.0.0
+  __TEXT.__text: 0x3089c
   __TEXT.__objc_methlist: 0x454
-  __TEXT.__const: 0x1242
+  __TEXT.__const: 0x1258
   __TEXT.__cstring: 0x83f
   __TEXT.__swift5_typeref: 0x6fc
   __TEXT.__swift5_fieldmd: 0x384

   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x88
   __TEXT.__swift5_types: 0x38
+  __TEXT.__oslogstring: 0x100b
   __TEXT.__swift5_capture: 0x97c
-  __TEXT.__oslogstring: 0xf7b
   __TEXT.__swift_as_entry: 0xac
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xa8
-  __TEXT.__unwind_info: 0xc28
+  __TEXT.__unwind_info: 0xc38
   __TEXT.__eh_frame: 0x16c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__const: 0x1360
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0xa90
-  __AUTH_CONST.__auth_got: 0x8f0
+  __AUTH_CONST.__auth_got: 0x8f8
   __AUTH.__objc_data: 0x538
   __AUTH.__data: 0x218
-  __DATA.__data: 0x5c8
+  __DATA.__data: 0x5d8
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 812
+  Functions: 819
   Symbols:   563
-  CStrings:  158
+  CStrings:  159
 
CStrings:
+ "MediaOutputDevice '%{private}s' declares realtimeVideoStreaming without realtimeAudioStreaming, which is not a supported combination."
```
