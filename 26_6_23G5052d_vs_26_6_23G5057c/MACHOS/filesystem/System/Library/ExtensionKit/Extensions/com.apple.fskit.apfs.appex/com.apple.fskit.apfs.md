## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-  __TEXT.__text: 0xdf540
+  __TEXT.__text: 0xdf6d0
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_stubs: 0x11e0
   __TEXT.__objc_methlist: 0x83c
   __TEXT.__const: 0x8ad0
-  __TEXT.__cstring: 0x3a19d
+  __TEXT.__cstring: 0x3a321
   __TEXT.__objc_methname: 0x1da3
   __TEXT.__oslogstring: 0x1ca4
   __TEXT.__objc_classname: 0x129
   __TEXT.__objc_methtype: 0x305f
   __TEXT.__gcc_except_tab: 0x484
-  __TEXT.__unwind_info: 0x1b20
+  __TEXT.__unwind_info: 0x1b28
   __DATA_CONST.__auth_got: 0x7c8
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x80

   __DATA.__objc_selrefs: 0x6d8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1300
+  __DATA.__data: 0x1308
   __DATA.__common: 0x7e0
   __DATA.__bss: 0x1e241
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3169
+  Functions: 3170
   Symbols:   1515
-  CStrings:  5288
+  CStrings:  5294
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__bss : content changed
CStrings:
+ "%s:%d: %s failed to clean-up proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
+ "%s:%d: %s failed to enter tx to store proposed wvek record, err = %d\n"
+ "%s:%d: %s failed to enter tx to update wvek record, err = %d\n"
+ "%s:%d: %s failed to flush tx storing proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to store proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to update wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s found existing proposed wvek record in nx keybag (from previous failure)\n"
+ "%s:%d: failed to lookup existing proposed wvek record in nx keybag, err = %d\n"
+ "2811.160.7"
+ "apfs_vek_commit_internal"
+ "kb"
- "%s:%d: failed to add proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to clean-up proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
- "%s:%d: failed to update wvek record in nx keybag, err = %d\n"
- "2811.160.6"
- "apfs_commit_update_volume_key"

```
