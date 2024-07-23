## locationpushd

> `/usr/libexec/locationpushd`

```diff

-2946.0.27.0.3
-  __TEXT.__text: 0x3df4
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0x88
+2946.0.30.0.0
+  __TEXT.__text: 0x42e4
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x244
+  __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x24e
   __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__objc_methname: 0x100e
-  __TEXT.__oslogstring: 0x96d
+  __TEXT.__objc_methname: 0x105f
+  __TEXT.__oslogstring: 0xce5
   __TEXT.__objc_classname: 0x71
-  __TEXT.__objc_methtype: 0x498
-  __TEXT.__info_plist: 0x550
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x1f0
+  __TEXT.__objc_methtype: 0x4a9
+  __TEXT.__info_plist: 0x54c
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__cfstring: 0x220

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x8c0
-  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_selrefs: 0x378
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1a0

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 69
-  Symbols:   96
-  CStrings:  277
+  Functions: 70
+  Symbols:   98
+  CStrings:  287
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
CStrings:
+ "Not adding topic due to unknown list"
+ "_addOrMoveTopic:forConnection:toList:"
+ "containsObject:"
+ "moveTopic:fromList:toList:"
+ "v40@0:8@16@24Q32"
+ "{\"msg%!{(MISSING)public}.0s\":\"Adding topic to ignored list\", \"topic\":%!{(MISSING)public, location:escape_only}@, \"connection\":%!{(MISSING)public, location:escape_only}@}"
+ "{\"msg%!{(MISSING)public}.0s\":\"Adding topic to opportunistic list\", \"topic\":%!{(MISSING)public, location:escape_only}@, \"connection\":%!{(MISSING)public, location:escape_only}@}"
+ "{\"msg%!{(MISSING)public}.0s\":\"Moving topic from ignored list connection\", \"topic\":%!{(MISSING)public, location:escape_only}@, \"connection\":%!{(MISSING)public, location:escape_only}@, \"toList\":%!{(MISSING)public}lu}"
+ "{\"msg%!{(MISSING)public}.0s\":\"Moving topic from opportunisitic list connection\", \"topic\":%!{(MISSING)public, location:escape_only}@, \"connection\":%!{(MISSING)public, location:escape_only}@, \"toList\":%!{(MISSING)public}lu}"
+ "{\"msg%!{(MISSING)public}.0s\":\"Not adding to IgnoredTopics since it's already an added topic\", \"topic\":%!{(MISSING)public, location:escape_only}@}"
+ "{\"msg%!{(MISSING)public}.0s\":\"Not adding to OpportunisticTopics since it's already an added topic\", \"topic\":%!{(MISSING)public, location:escape_only}@}"
+ "{\"msg%!{(MISSING)public}.0s\":\"Not adding topic due to unknown list\", \"toList\":%!{(MISSING)public}lu}"
- "Moving topic %!{(MISSING)public}@ to ignored list connection %!{(MISSING)public}@"
- "Moving topic %!{(MISSING)public}@ to opportunisitic list connection %!{(MISSING)public}@"

```
