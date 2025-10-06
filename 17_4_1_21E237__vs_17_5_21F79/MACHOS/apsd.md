## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-971.500.141.0.0
-  __TEXT.__text: 0xbd284
+971.600.51.0.0
+  __TEXT.__text: 0xbd7f4
   __TEXT.__auth_stubs: 0x1f40
-  __TEXT.__objc_stubs: 0xfae0
+  __TEXT.__objc_stubs: 0xfb20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x9ae8
-  __TEXT.__objc_methname: 0x191f3
+  __TEXT.__objc_methlist: 0x9b00
+  __TEXT.__objc_methname: 0x19215
   __TEXT.__objc_classname: 0xf4d
   __TEXT.__objc_methtype: 0x4212
   __TEXT.__cstring: 0x8e02
   __TEXT.__const: 0x6aa
-  __TEXT.__oslogstring: 0x10616
+  __TEXT.__oslogstring: 0x106ab
   __TEXT.__gcc_except_tab: 0x1bf0
   __TEXT.__dlopen_cstrs: 0x100
   __TEXT.__constg_swiftt: 0x238

   __TEXT.__swift5_reflstr: 0x199
   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3010
+  __TEXT.__unwind_info: 0x3118
   __TEXT.__eh_frame: 0x118
   __DATA_CONST.__auth_got: 0xfb8
   __DATA_CONST.__got: 0x488

   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x1cd48
-  __DATA.__objc_selrefs: 0x5110
+  __DATA.__objc_selrefs: 0x5120
   __DATA.__objc_ivar: 0xca4
   __DATA.__objc_data: 0x2d38
   __DATA.__data: 0x17f8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6B026EEE-A839-3D1C-9338-9EFF46F16C5F
-  Functions: 4604
+  UUID: A3128CFA-2D43-3112-8E85-266F320C7587
+  Functions: 4606
   Symbols:   752
-  CStrings:  8058
+  CStrings:  8061
 
CStrings:
+ "%@ Schedule server update with change %@; withTimer %@; shortInterval %@; isPowerEfficientToSendFilter %@"
+ "%@ Topic change is low priority, not scheduling a timer."
+ "%@ no change detected between the new filter and the old server filter - cancelling any pending updates"
+ "%@: calculated change type for %@ {newTopicFilter: %d, previouslyChosenTopicFilter: %d, previousServerTopicFilter: %d change: %@}"
+ "%@: completed transaction - calculated change %@ {topics changed: %@}"
+ "T@\"NSMutableArray\",&,N,V_topicsChanged"
+ "_scheduleServerUpdateWithChange:timer:shortInterval:"
+ "_topicsChanged"
+ "currentFilterForTopicState:"
+ "setTopicsChanged:"
+ "topicsChanged"
- "%@ asked to schedule an update withTimer? %@"
- "%@ no change detected between the new and old server filter - cancelling any pending updates"
- "%@: calculated change type for %@ {newTopicFilter: %d, previouslyChosenTopicFilter: %d, change: %@}"
- "%@: completed transaction - calculated change %@ {initialFilterByTopicName: %@}"
- "T@\"NSMutableDictionary\",&,N,V_initialFilterByTopicName"
- "_initialFilterByTopicName"
- "initialFilterByTopicName"
- "setInitialFilterByTopicName:"

```
