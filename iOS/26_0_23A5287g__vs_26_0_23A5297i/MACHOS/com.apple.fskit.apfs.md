## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0xa7030
+2632.0.68.0.3
+  __TEXT.__text: 0xa73c8
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x88f0
-  __TEXT.__cstring: 0x2de79
+  __TEXT.__cstring: 0x2dfb7
   __TEXT.__gcc_except_tab: 0x78
   __TEXT.__oslogstring: 0x11b
   __TEXT.__objc_classname: 0x5b

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: C0E4D69F-411D-38E1-AB8D-22CEF14A4F9A
-  Functions: 2324
+  UUID: AEE5554C-6CDD-32F4-BCB3-DE0808D39340
+  Functions: 2325
   Symbols:   1192
-  CStrings:  3953
+  CStrings:  3959
 
CStrings:
+ "!(flags & ~(BT_MODIFY | BT_LOCK | BT_IGNORE_CORRUPT | BT_RAGE | BT_CACHED | BT_ASYNC | BT_PREFETCH))"
+ "!(flags & ~(BT_MODIFY | BT_LOCK | BT_IGNORE_CORRUPT | BT_RAGE))"
+ "!(flags & ~(OBJECT_TYPE_FLAGS_DEFINED_MASK | OBJ_LOCK | OBJ_MODIFY | OBJ_MODIFY_ALLOC | OBJ_OXID_MATCH | OBJ_PLACEHOLDER | OBJ_IGNORE_CORRUPT | OBJ_NOCACHE | OBJ_RAGE | OBJ_ASYNC | OBJ_PREFETCH | OBJ_RAW_ENCRYPTED | OBJ_CRYPTO_KEY_INDEX_MASK | OBJ_CRYPTO_TWEAK_TYPE_MASK))"
+ "!(flags & ~(OBJECT_TYPE_FLAGS_DEFINED_MASK | OBJ_NOCACHE | OBJ_RAGE | OBJ_LOCK | OBJ_CRYPTO_KEY_INDEX_MASK | OBJ_CRYPTO_TWEAK_TYPE_MASK))"
+ "!(oflags & ~(OBJECT_TYPE_FLAGS_DEFINED_MASK | OBJ_CRYPTO_KEY_INDEX_MASK | OBJ_CRYPTO_TWEAK_TYPE_MASK | OBJ_RAGE))"
+ "%s:%d: %s dirty object in rage free list\n"
+ "%s:%d: %s ephemeral object in rage free list\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n"
+ "%s:%d: %s fs object in rage free list\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
+ "%s:%d: %s rage free list count mismatch %d != %d\n"
+ "%s:%d: %s referenced object in rage free list\n"
+ "2632.0.68.0.3"
+ "oc->oc_rage_free_count > 0"
- "!(flags & ~(BT_MODIFY | BT_LOCK | BT_IGNORE_CORRUPT | BT_NOCACHE | BT_CACHED | BT_ASYNC | BT_PREFETCH))"
- "!(flags & ~(BT_MODIFY | BT_LOCK | BT_IGNORE_CORRUPT | BT_NOCACHE))"
- "!(flags & ~(OBJECT_TYPE_FLAGS_DEFINED_MASK | OBJ_LOCK | OBJ_CRYPTO_KEY_INDEX_MASK | OBJ_CRYPTO_TWEAK_TYPE_MASK))"
- "!(flags & ~(OBJECT_TYPE_FLAGS_DEFINED_MASK | OBJ_LOCK | OBJ_MODIFY | OBJ_MODIFY_ALLOC | OBJ_OXID_MATCH | OBJ_PLACEHOLDER | OBJ_IGNORE_CORRUPT | OBJ_NOCACHE | OBJ_ASYNC | OBJ_PREFETCH | OBJ_CRYPTO_KEY_INDEX_MASK | OBJ_CRYPTO_TWEAK_TYPE_MASK))"
- "!(oflags & ~(OBJECT_TYPE_FLAGS_DEFINED_MASK | OBJ_CRYPTO_KEY_INDEX_MASK | OBJ_CRYPTO_TWEAK_TYPE_MASK))"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error allocating new physical location %d\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n"
- "%s:%d: %s oid 0x%llx flags 0x%x type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
- "2632.0.54.0.2"

```
