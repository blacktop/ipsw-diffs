## DeviceActivityConductor

> `/System/Library/PrivateFrameworks/DeviceActivityConductor.framework/DeviceActivityConductor`

```diff

-24.0.3.0.0
-  __TEXT.__text: 0xacb8
+24.10.7.0.0
+  __TEXT.__text: 0xad28
   __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_methlist: 0x778
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x570
-  __TEXT.__gcc_except_tab: 0x3a4
-  __TEXT.__oslogstring: 0x822
+  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__oslogstring: 0x94a
   __TEXT.__unwind_info: 0x3f4
   __TEXT.__objc_classname: 0x167
-  __TEXT.__objc_methname: 0x108d
-  __TEXT.__objc_methtype: 0x423
+  __TEXT.__objc_methname: 0x109f
+  __TEXT.__objc_methtype: 0x431
   __TEXT.__objc_stubs: 0xcc0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x420

   - /usr/lib/libobjc.A.dylib
   Functions: 229
   Symbols:   961
-  CStrings:  409
+  CStrings:  410
 
Symbols:
+ -[DACActivityList changesFromList:includingMetadata:]
+ ___53-[DACActivityList changesFromList:includingMetadata:]_block_invoke
+ ___53-[DACActivityList changesFromList:includingMetadata:]_block_invoke_2
+ ___53-[DACActivityList changesFromList:includingMetadata:]_block_invoke_3
+ ___block_descriptor_73_e8_32s40s48s56r64r_e56_v32?0"NSOrderedSet"8"NSOrderedSet"16"NSOrderedSet"24ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
+ _objc_msgSend$changesFromList:includingMetadata:
- -[DACActivityList changesFromList:]
- ___35-[DACActivityList changesFromList:]_block_invoke
- ___35-[DACActivityList changesFromList:]_block_invoke_2
- ___35-[DACActivityList changesFromList:]_block_invoke_3
- ___block_descriptor_72_e8_32s40s48s56r64r_e56_v32?0"NSOrderedSet"8"NSOrderedSet"16"NSOrderedSet"24ls32l8r56l8s40l8s48l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
- _objc_msgSend$changesFromList:
CStrings:
+ "%p activating assertion %p for %{public}@ with %{public}@"
+ "%p activity %{public}@ already in list, removing it"
+ "%p activity %{public}@ not in list, unable to remove it"
+ "%p added activity %{public}@ to list"
+ "%p created role %{public}@"
+ "%p delta common(%{public}@) add(%{public}@) remove(%{public}@) from %p to %p"
+ "%p determined state(%lu) for Activity(%{public}@)"
+ "%p insert index %lu for %{public}@"
+ "%p merge result %{public}@ from %{public}@ into %{public}@"
+ "%p no assertion for %{public}@ with %{public}@ to activate"
+ "%p not activating assertion %p in invalid state %lu for %{public}@ with %{public}@"
+ "%p now %lu (%lu unique) assertions after creating %p for %{public}@"
+ "%p now %lu (%lu unique) assertions after deactivation of %{public}@"
+ "%p now %lu (%lu unique) assertions after relinquish of %p for %{public}@"
+ "%p now %lu (%lu unique) assertions remain for %{public}@"
+ "%p now %lu unique assertions after last assertion removal for %{public}@"
+ "%p offline relinquish of %{public}@"
+ "%p removed activity %{public}@ from list due to %{public}@"
+ "%p removing assertion %p at %lu for %{public}@"
+ "%p requesting deactivation of non-active activity %{public}@"
+ "%p role changing to %{public}@ from %{public}@"
+ "%p unable to locate assertion %p for %{public}@"
+ "%p update reason of %{public}@ at %lu to %lu"
+ "@28@0:8@16B24"
+ "Change Marker missing, using %{public}@"
+ "Compare yielded %ld for %{public}@ and %{public}@"
+ "changesFromList:includingMetadata:"
+ "offline activation of %{public}@"
+ "offline deactivation of %{public}@"
- "%p activating assertion %p for %@ with %@"
- "%p activity %@ already in list, removing it"
- "%p activity %@ not in list, unable to remove it"
- "%p added activity %@ to list"
- "%p created role %@"
- "%p delta common(%@) add(%@) remove(%@) from %p to %p"
- "%p determined state(%lu) for Activity(%@)"
- "%p insert index %lu for %@"
- "%p merge result %@ from %@ into %@"
- "%p no assertion for %@ with %@ to activate"
- "%p not activating assertion %p in invalid state %lu for %@ with %@"
- "%p now %lu (%lu unique) assertions after creating %p for %@"
- "%p now %lu (%lu unique) assertions after deactivation of %@"
- "%p now %lu (%lu unique) assertions after relinquish of %p for %@"
- "%p now %lu (%lu unique) assertions remain for %@"
- "%p now %lu unique assertions after last assertion removal for %@"
- "%p offline relinquish of %@"
- "%p removed activity %@ from list due to %@"
- "%p removing assertion %p at %lu for %@"
- "%p requesting deactivation of non-active activity %@"
- "%p role changing to %@ from %@"
- "%p unable to locate assertion %p for %@"
- "%p update reason of %@ at %lu to %lu"
- "Change Marker missing, using %@"
- "Compare yielded %ld for %@ and %@"
- "changesFromList:"
- "offline activation of %@"
- "offline deactivation of %@"

```
