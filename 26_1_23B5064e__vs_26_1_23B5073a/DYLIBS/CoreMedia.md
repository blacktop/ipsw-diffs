## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3285.9.1.0.0
-  __TEXT.__text: 0x1b8440
+3285.11.1.3.0
+  __TEXT.__text: 0x1b8e48
   __TEXT.__auth_stubs: 0x34a0
   __TEXT.__objc_methlist: 0x5d4
-  __TEXT.__const: 0x1b28
-  __TEXT.__cstring: 0x1efee
-  __TEXT.__oslogstring: 0x62b0
+  __TEXT.__const: 0x1b38
+  __TEXT.__cstring: 0x1f038
+  __TEXT.__oslogstring: 0x64a6
   __TEXT.__gcc_except_tab: 0x1a0
   __TEXT.__dlopen_cstrs: 0x190
-  __TEXT.__unwind_info: 0x4c08
+  __TEXT.__unwind_info: 0x4c10
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0x104
-  __TEXT.__objc_methname: 0x18f4
-  __TEXT.__objc_methtype: 0xbbe
+  __TEXT.__objc_methname: 0x18fc
+  __TEXT.__objc_methtype: 0xbc9
   __TEXT.__objc_stubs: 0x1680
   __DATA_CONST.__got: 0x520
   __DATA_CONST.__const: 0xa368

   __DATA.__data: 0xa39
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x13e0
-  __DATA.__common: 0x300
+  __DATA.__common: 0x320
   __DATA_DIRTY.__data: 0x324
   __DATA_DIRTY.__common: 0x128
   __DATA_DIRTY.__bss: 0x18c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7D996112-85D0-3EAB-B3E6-EF3B67A054B4
+  UUID: 6BC2D385-7DF4-3CA2-A9B4-93D65B25CF24
   Functions: 9641
-  Symbols:   22688
-  CStrings:  8672
+  Symbols:   22689
+  CStrings:  8676
 
Symbols:
+ _gFigTimeRangeTrace
Functions:
~ _CMAudioFormatDescriptionCreateSummary : 1268 -> 1264
~ _CMSpeedRampMapTimeFromTargetToSource : 1188 -> 2260
~ _CMSpeedRampMapTimeFromSourceToTarget : 1176 -> 2216
~ _CMVideoFormatDescriptionCopyTagCollectionArray : 932 -> 1392
CStrings:
+ "<<< FigTimeRange >>> %s: binary search failure: t %1.3f, mappingCount %d, mappingArray[0] source %1.3f...%1.3f, mappingArray[%d] %1.3f...%1.3f, mappingArray[%d] %1.3f...%1.3f, mappingArray[%d] %1.3f...%1.3f, minIndex %d, maxIndex %d, numIterations %d"
+ "<<< FigTimeRange >>> %s: binary search failure: t %1.3f, mappingCount %d, mappingArray[0] target %1.3f...%1.3f, mappingArray[%d] %1.3f...%1.3f, mappingArray[%d] %1.3f...%1.3f, mappingArray[%d] %1.3f...%1.3f, minIndex %d, maxIndex %d, numIterations %d"
+ "CMSpeedRampMapTimeFromSourceToTarget"
+ "CMSpeedRampMapTimeFromTargetToSource"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
