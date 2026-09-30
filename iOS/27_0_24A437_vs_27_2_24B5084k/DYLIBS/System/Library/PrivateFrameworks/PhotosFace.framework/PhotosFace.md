## PhotosFace

> `/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace`

```diff

-96.0.0.0.0
-  __TEXT.__text: 0xc57e8
-  __TEXT.__const: 0x7c18
+98.0.0.0.0
+  __TEXT.__text: 0xc5d30
+  __TEXT.__const: 0x7c28
   __TEXT.__swift5_typeref: 0x23ad
-  __TEXT.__cstring: 0x400c
+  __TEXT.__cstring: 0x40fc
   __TEXT.__swift5_reflstr: 0x13b4
   __TEXT.__swift5_assocty: 0x5d8
   __TEXT.__constg_swiftt: 0x2f24

   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_proto: 0x524
   __TEXT.__swift5_types: 0x25c
-  __TEXT.__swift_as_entry: 0x3fc
-  __TEXT.__swift_as_ret: 0x328
-  __TEXT.__swift_as_cont: 0x720
+  __TEXT.__swift_as_entry: 0x400
+  __TEXT.__swift_as_ret: 0x340
+  __TEXT.__swift_as_cont: 0x730
   __TEXT.__swift5_capture: 0x8e4
   __TEXT.__swift5_protos: 0x28
   __TEXT.__oslogstring: 0x80f
   __TEXT.__unwind_info: 0x4608
-  __TEXT.__eh_frame: 0xab68
+  __TEXT.__eh_frame: 0xab80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4283
+  Functions: 4284
   Symbols:   1127
   CStrings:  234
 
Symbols:
+ ___swift_closure_destructor.203Tm
+ ___swift_closure_destructor.238Tm
- ___swift_closure_destructor.201Tm
- ___swift_closure_destructor.236Tm
CStrings:
+ "    DELETE FROM tracked_album_photos\n    WHERE\n        CASE WHEN day > ? THEN day/? ELSE day END >= ?      -- rdar://145093387\n        AND CASE WHEN day > ? THEN day/? ELSE day END <= ?  -- rdar://145093387\n        AND album_id = ?"
+ "    DELETE FROM tracked_gallery_photos\n    WHERE\n        CASE WHEN day > ? THEN day/? ELSE day END >= ?      -- rdar://145093387\n        AND CASE WHEN day > ? THEN day/? ELSE day END <= ?  -- rdar://145093387\n        AND gallery_id = ?"
+ "    DELETE FROM tracked_shuffle_photos\n    WHERE\n        CASE WHEN day > ? THEN day/? ELSE day END >= ?      -- rdar://145093387\n        AND CASE WHEN day > ? THEN day/? ELSE day END <= ?  -- rdar://145093387\n        AND shuffle_id = ?"
- "    DELETE FROM tracked_album_photos\n    WHERE\n        CASE WHEN day > ? THEN day/? ELSE day END < ?  -- rdar://145093387\n        AND album_id = ?"
- "    DELETE FROM tracked_gallery_photos\n    WHERE\n        CASE WHEN day > ? THEN day/? ELSE day END < ?  -- rdar://145093387\n        AND gallery_id = ?"
- "    DELETE FROM tracked_shuffle_photos\n    WHERE\n        CASE WHEN day > ? THEN day/? ELSE day END < ?  -- rdar://145093387\n        AND shuffle_id = ?"
```
