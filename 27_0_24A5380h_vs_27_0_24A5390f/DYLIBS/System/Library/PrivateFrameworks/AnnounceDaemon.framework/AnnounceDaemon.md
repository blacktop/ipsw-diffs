## AnnounceDaemon

> `/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-329.0.0.0.0
-  __TEXT.__text: 0x560dc
-  __TEXT.__objc_methlist: 0x370c
+331.0.0.0.0
+  __TEXT.__text: 0x563f4
+  __TEXT.__objc_methlist: 0x3734
   __TEXT.__const: 0x1988
   __TEXT.__cstring: 0x22d4
-  __TEXT.__oslogstring: 0x56d8
+  __TEXT.__oslogstring: 0x5758
   __TEXT.__gcc_except_tab: 0xb0c
   __TEXT.__constg_swiftt: 0x350
   __TEXT.__swift5_typeref: 0xa60

   __TEXT.__swift5_assocty: 0x210
   __TEXT.__swift5_proto: 0x148
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x16c0
+  __TEXT.__unwind_info: 0x16c8
   __TEXT.__eh_frame: 0x8a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2778
+  __DATA_CONST.__objc_selrefs: 0x2788
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__got: 0x8d8
   __AUTH_CONST.__const: 0x14c0
   __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x4f88
+  __AUTH_CONST.__objc_const: 0x4f90
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x9c8
   __AUTH.__objc_data: 0x738

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1842
-  Symbols:   3956
-  CStrings:  795
+  Functions: 1845
+  Symbols:   3960
+  CStrings:  798
 
Symbols:
+ -[ANUserNotificationController _removeNotificationWithRequestID:]
+ -[ANUserNotificationController removeNotificationForAnnouncementsWithID:groupID:]
+ _objc_msgSend$_removeNotificationWithRequestID:
+ _objc_msgSend$removeNotificationForAnnouncementsWithID:groupID:
Functions:
+ -[ANUserNotificationController removeNotificationForAnnouncementsWithID:groupID:]
+ -[ANUserNotificationController _removeNotificationWithRequestID:]
~ -[ANAnnouncementManager _removeAnnouncementWithID:] : 580 -> 800
+ -[ANAnnouncementManager _removeAnnouncementWithID:].cold.1
CStrings:
+ "%@Removing user notification %@ in group %@"
+ "%@Trying to removing user notification null ID"
+ "Trying to remove notification with null group ID"
```
