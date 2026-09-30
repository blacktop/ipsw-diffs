## com.apple.fskit.exfat

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat`

```diff

-463.0.1.0.0
-  __TEXT.__text: 0xe484
+463.60.7.0.0
+  __TEXT.__text: 0xe354
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0x4ca3
-  __TEXT.__cstring: 0x2e4f
-  __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__objc_methname: 0x7b9
+  __TEXT.__cstring: 0x2e2d
+  __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__objc_methname: 0x789
   __TEXT.__oslogstring: 0x531
   __TEXT.__objc_classname: 0x77
-  __TEXT.__objc_methtype: 0x30b
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__objc_methtype: 0x2e0
+  __TEXT.__unwind_info: 0x270
   __DATA_CONST.__auth_got: 0x448
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   - /usr/lib/libutil.dylib
   Functions: 237
   Symbols:   320
-  CStrings:  500
+  CStrings:  499
 
CStrings:
+ "-[exfatFileSystem syncRead:into:startingAt:length:]"
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
+ "@40@0:8@16@24^@32"
+ "readInto:startingAt:length:error:"
+ "startCheckWithTask:parameters:error:"
+ "startFormatWithTask:parameters:error:"
- "-[exfatFileSystem syncRead:into:startingAt:length:]_block_invoke"
- "checkWithParameters:connection:taskID:replyHandler:"
- "formatWithParameters:connection:taskID:replyHandler:"
- "synchronousReadInto:startingAt:length:replyHandler:"
- "v24@?0Q8@\"NSError\"16"
- "v48@0:8@\"NSArray\"16@\"FSMessageConnection\"24@\"NSUUID\"32@?<v@?@\"NSProgress\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
