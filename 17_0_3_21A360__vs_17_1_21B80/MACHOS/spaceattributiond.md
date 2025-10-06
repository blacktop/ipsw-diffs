## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-175.2.1.0.0
-  __TEXT.__text: 0x24be4
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_stubs: 0x3b80
-  __TEXT.__objc_methlist: 0x156c
-  __TEXT.__gcc_except_tab: 0x112c
-  __TEXT.__oslogstring: 0x2c22
-  __TEXT.__cstring: 0x2256
-  __TEXT.__objc_methname: 0x4346
-  __TEXT.__objc_classname: 0x204
-  __TEXT.__objc_methtype: 0xba2
-  __TEXT.__const: 0x60
-  __TEXT.__unwind_info: 0x818
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x70
+180.42.1.0.0
+  __TEXT.__text: 0x25b38
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_stubs: 0x3ca0
+  __TEXT.__objc_methlist: 0x16b8
+  __TEXT.__gcc_except_tab: 0x114c
+  __TEXT.__oslogstring: 0x2d17
+  __TEXT.__cstring: 0x2304
+  __TEXT.__objc_methname: 0x4629
+  __TEXT.__objc_classname: 0x213
+  __TEXT.__objc_methtype: 0xc1d
+  __TEXT.__const: 0x70
+  __TEXT.__unwind_info: 0x834
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x1aa0
-  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__cfstring: 0x1b20
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x2920
-  __DATA.__objc_selrefs: 0x1230
+  __DATA.__objc_const: 0x2b88
+  __DATA.__objc_selrefs: 0x12c8
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x200
-  __DATA.__objc_superrefs: 0x68
-  __DATA.__objc_ivar: 0x190
-  __DATA.__objc_data: 0x820
+  __DATA.__objc_classrefs: 0x208
+  __DATA.__objc_superrefs: 0x70
+  __DATA.__objc_ivar: 0x1b8
+  __DATA.__objc_data: 0x870
   __DATA.__data: 0x248
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0xf0
   __DATA.__common: 0x1
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E37867C-945F-3736-8EBE-495FAE8685C7
-  Functions: 821
-  Symbols:   196
-  CStrings:  1727
+  UUID: 3501CC68-3AC1-31A4-BC95-E4109759EF98
+  Functions: 851
+  Symbols:   193
+  CStrings:  1780
 
Symbols:
+ _dispatch_apply
- __dispatch_queue_attr_concurrent
- _dispatch_async
- _dispatch_queue_attr_make_with_qos_class
- _dispatch_queue_create
CStrings:
+ "\x01\x13\xa2"
+ "\x16\x12\x11"
+ "%@: Path (%@) dir-stat clone size (%lld) is greater than dir-stat physical size (%lld)"
+ "%@: Path (%@) dir-stat cloneSize %lld > physicalSize: %lld"
+ "%s can't malloc %llu bytes"
+ "%s path %@, data %llu, clone %llu, purge %llu"
+ "%s statfs returned %d"
+ "+[SACloneTreeWalker isNodeID:oldestForDStreamID:forVolPath:]"
+ "1"
+ "@32@0:8Q16@24"
+ "@32@0:8Q16^{fsid=[2i]}24"
+ "@48@0:8q16q24q32@40"
+ "B40@0:8Q16Q24@32"
+ "Bundle %@ ParentBundle %@"
+ "SACloneInfo"
+ "START: zeroSizeAppsFiltering"
+ "T@\"NSMutableArray\",&,V_clonesInfo"
+ "T@\"NSMutableSet\",&,V_knownDstreamIDs"
+ "T@\"NSMutableSet\",&,V_knownInodeIDs"
+ "T@\"NSString\",&,V_clonePath"
+ "TB,V_isActivity"
+ "_clonePath"
+ "_clonesInfo"
+ "_fs_num"
+ "_isActivity"
+ "_knownDstreamIDs"
+ "_knownInodeIDs"
+ "_purgeableFolder"
+ "addCloneInfo:"
+ "addClonePathOfCloneID:FSId:dataSize:purgeableSize:bundleSet:cloneData:"
+ "arrayWithObjects:count:"
+ "clonePath"
+ "clonesInfo"
+ "daily-activity-time-info"
+ "fsgetpath returned errno %d for nodeID %llu"
+ "getParentOfBundle:"
+ "getPathOfNodeID:FSid:"
+ "initWithDataSize:cloneSize:purgeableSize:clonePath:"
+ "initWithSAFOptions:withActivity:"
+ "isActivity"
+ "isNodeID:oldestForDStreamID:forVolPath:"
+ "knownDstreamIDs"
+ "knownInodeIDs"
+ "lastDailyActivitySentTelemetryDate"
+ "lastUserSentTelemetryDate"
+ "newWithDataSize:cloneSize:purgeableSize:clonePath:"
+ "newWithSAFOptions:withActivity:"
+ "processCloneMapOnVol buffSize 0 : No clones in volume %@"
+ "processCloneMapOnVol:withPathList:collectClonesPaths:reply:"
+ "removeAllObjects"
+ "setClonePath:"
+ "setClonesInfo:"
+ "setIsActivity:"
+ "setKnownDstreamIDs:"
+ "setKnownInodeIDs:"
+ "user-time-info"
+ "v16@?0Q8"
+ "v44@0:8@16@24B32@?36"
+ "v64@0:8Q16^{fsid=[2i]}24Q32Q40@48@56"
+ "zeroSizeAppsFiltering"
- "\x01\x13"
- "\x06\x12\x11"
- "@24@0:8Q16"
- "com.apple.spaceattributiond.queue"
- "fsgetpath returned errno %d for %s"
- "initWithSAFOptions:"
- "lastSentTelemetryDate"
- "newWithSAFOptions:"
- "processCloneMapOnVol buff_size 0 : No clones in volume %@"
- "processCloneMapOnVol:withPathList:reply:"
- "searchAppsListForBundle:"
- "time-info"

```
