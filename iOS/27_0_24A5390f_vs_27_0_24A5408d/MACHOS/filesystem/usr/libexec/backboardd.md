## backboardd

> `/usr/libexec/backboardd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`

```diff

-873.100.0.0.0
-  __TEXT.__text: 0x58298
+877.0.0.0.0
+  __TEXT.__text: 0x58a64
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_stubs: 0x9e20
-  __TEXT.__objc_methlist: 0x49a4
+  __TEXT.__objc_stubs: 0x9e80
+  __TEXT.__objc_methlist: 0x4a0c
   __TEXT.__const: 0x320
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__gcc_except_tab: 0x770
-  __TEXT.__objc_methname: 0xdb53
-  __TEXT.__objc_classname: 0x1368
-  __TEXT.__cstring: 0x4c7f
-  __TEXT.__objc_methtype: 0x2eb6
-  __TEXT.__oslogstring: 0x704c
-  __TEXT.__unwind_info: 0x15c8
-  __DATA_CONST.__const: 0x32f0
-  __DATA_CONST.__cfstring: 0x5020
-  __DATA_CONST.__objc_classlist: 0x330
-  __DATA_CONST.__objc_protolist: 0x230
+  __TEXT.__objc_methname: 0xdbe8
+  __TEXT.__objc_classname: 0x13c1
+  __TEXT.__cstring: 0x4cd3
+  __TEXT.__objc_methtype: 0x2ed7
+  __TEXT.__oslogstring: 0x7144
+  __TEXT.__unwind_info: 0x15e0
+  __DATA_CONST.__const: 0x3318
+  __DATA_CONST.__cfstring: 0x5000
+  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x268
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xab8
-  __DATA_CONST.__got: 0x890
+  __DATA_CONST.__got: 0x898
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xad88
-  __DATA.__objc_selrefs: 0x30c8
-  __DATA.__objc_ivar: 0x7f0
-  __DATA.__objc_data: 0x1fe0
-  __DATA.__data: 0x1ac8
-  __DATA.__bss: 0x328
+  __DATA.__objc_const: 0xaf20
+  __DATA.__objc_selrefs: 0x30e8
+  __DATA.__objc_ivar: 0x7fc
+  __DATA.__objc_data: 0x2030
+  __DATA.__data: 0x1b88
+  __DATA.__bss: 0x340
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 1897
-  Symbols:   617
-  CStrings:  4079
+  Functions: 1904
+  Symbols:   618
+  CStrings:  4091
 
Symbols:
+ _BKSDisplayServiceName
CStrings:
+ "%s %{public}@ Blanked: %{BOOL}u"
+ "%s Blanked: %{BOOL}u"
+ "%s Blanked: %{BOOL}u -- suppressed - shell handles it"
+ "%{public}s: unknown displayUUID/systemDisplayIdentifier:%{public}@ "
+ "BKDisplayService: ignoring screen-blank suppression from non-system-shell client %{public}@"
+ "BKDisplayServiceServer"
+ "BKSDisplayServiceClientInterface"
+ "BKSDisplayServiceServerInterface"
+ "Vv24@0:8@\"NSSet<__NSString__>\"16"
+ "_connectionIsSystemShell:"
+ "_publishLock"
+ "_publishScreenBlankNotificationSuppressedDisplays"
+ "com.apple.backboardd.BKDisplayServiceServer"
+ "hasBlankedScreen notification suppressed for displays: %{public}@"
+ "setScreenBlankNotificationSuppressedDisplayUUIDs:"
+ "unionSet:"
+ "v24@?0@\"BSServiceConnection\"8@\"NSMutableSet\"16"
- "%s %{public}@ Blanked: %@"
- "%s Blanked: %@"
- "%{public}s: unknown displayUUID:%{public}@ "
- "NO"
- "YES"
```
