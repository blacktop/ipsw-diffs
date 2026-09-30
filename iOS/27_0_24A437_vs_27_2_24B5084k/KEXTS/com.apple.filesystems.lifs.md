## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-974.0.13.0.2
-  __TEXT.__os_log: 0x1f5d
-  __TEXT.__cstring: 0x29fa
-  __TEXT.__const: 0x338
-  __TEXT_EXEC.__text: 0x20598
+974.40.11.0.0
+  __TEXT.__os_log: 0x1ffc
+  __TEXT.__cstring: 0x2a13
+  __TEXT.__const: 0x348
+  __TEXT_EXEC.__text: 0x20a04
   __TEXT_EXEC.__auth_stubs: 0xfb0
   __DATA.__data: 0x578
   __DATA.__common: 0x138

   __DATA_CONST.__kalloc_type: 0xe40
   __DATA_CONST.__kalloc_var: 0xf0
   __DATA_CONST.__auth_got: 0x7d8
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 460
+  Functions: 463
   Symbols:   0
-  CStrings:  520
+  CStrings:  524
 
CStrings:
+ "\"%s: io_lock_override is already set for lnode %p by thread %p\" @%s:%d"
+ "\"%s: io_lock_override is not set for lnode %p\" @%s:%d"
+ "%s: attributes update returned error %d"
+ "%s: caught a signal, giving up with %d"
+ "%s: got %d from msleep, giving up with EIO"
+ "%s: request %llu was claimed by a reply while giving up with error %d, awaiting that reply's completion"
+ "%s: timed out, giving up with %d"
+ "111222222222222222122222222222222212111111111222222222222222211212222222112221"
+ "lifs_abandon_sync_req"
+ "lifs_update_attrs_if_needed"
- "\"%s: override is already set for lnode %p io_lock\" @%s:%d"
- "\"%s: override is not set for lnode %p io_lock\" @%s:%d"
- "%s: caught a signal, returning %d"
- "%s: got %d from msleep, returning EIO"
- "%s: timed out, returning %d"
- "11122222222222222222222222222222222222222222222222332222122222222222222212111111111222222222222222211212222222112221"
```
