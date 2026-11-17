## com.apple.AppleKeyStoreEvents

> `/System/Library/UserEventPlugins/com.apple.AppleKeyStoreEvents.plugin/com.apple.AppleKeyStoreEvents`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA.__const`

```diff

-2383.60.16.0.0
-  __TEXT.__text: 0x1684
+2383.60.16.0.1
+  __TEXT.__text: 0x174c
   __TEXT.__auth_stubs: 0x250
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x3a4
-  __TEXT.__oslogstring: 0x17c
+  __TEXT.__cstring: 0x3fc
+  __TEXT.__oslogstring: 0x1e2
   __TEXT.__unwind_info: 0x118
   __DATA.__const: 0xa8
   __DATA.__data: 0x4

   - /usr/lib/libSystem.B.dylib
   Functions: 55
   Symbols:   92
-  CStrings:  46
+  CStrings:  50
 
Functions:
~ sub_770 : 932 -> 1132
CStrings:
+ "KeyStoreNotifier posting convenience bio created"
+ "KeyStoreNotifier posting convenience bio unavailable"
+ "com.apple.keystore.conveniencebio.created"
+ "com.apple.keystore.conveniencebio.unavailable"
```
