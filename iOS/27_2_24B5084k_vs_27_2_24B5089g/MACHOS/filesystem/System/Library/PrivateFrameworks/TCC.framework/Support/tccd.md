## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-918.0.0.0.0
-  __TEXT.__text: 0x8d254
+919.0.0.0.0
+  __TEXT.__text: 0x8e498
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0xb980
-  __TEXT.__objc_methlist: 0x56b4
-  __TEXT.__cstring: 0x1347d
+  __TEXT.__objc_stubs: 0xbb60
+  __TEXT.__objc_methlist: 0x5754
+  __TEXT.__cstring: 0x1366f
   __TEXT.__const: 0x6f8
-  __TEXT.__gcc_except_tab: 0x3120
-  __TEXT.__objc_methname: 0x13533
-  __TEXT.__oslogstring: 0x10db2
+  __TEXT.__gcc_except_tab: 0x31fc
+  __TEXT.__objc_methname: 0x138f5
+  __TEXT.__oslogstring: 0x11095
   __TEXT.__objc_classname: 0x6f2
   __TEXT.__objc_methtype: 0x2383
-  __TEXT.__dlopen_cstrs: 0x90
-  __TEXT.__unwind_info: 0x2528
-  __DATA_CONST.__const: 0x28d8
-  __DATA_CONST.__cfstring: 0x8da0
+  __TEXT.__dlopen_cstrs: 0xd9
+  __TEXT.__unwind_info: 0x2580
+  __DATA_CONST.__const: 0x2920
+  __DATA_CONST.__cfstring: 0x8e40
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_intobj: 0x678
-  __DATA_CONST.__objc_arraydata: 0x1628
-  __DATA_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__objc_arraydata: 0x1630
+  __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0xf28
   __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0xa6c8
-  __DATA.__objc_selrefs: 0x37c0
-  __DATA.__objc_ivar: 0x764
+  __DATA.__objc_const: 0xa758
+  __DATA.__objc_selrefs: 0x3840
+  __DATA.__objc_ivar: 0x770
   __DATA.__objc_data: 0x13b0
   __DATA.__data: 0x738
   __DATA.__common: 0x30

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3077
-  Symbols:   510
-  CStrings:  6012
+  Functions: 3104
+  Symbols:   512
+  CStrings:  6055
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSNumberFormatter
CStrings:
+ "%s: %{public}@ accessed Health data %lu time(s) since %{public}@"
+ "%s: %{public}@ did not expand; falling back to the countless sentence"
+ "%s: HealthKit framework not available, no access count for %{public}@"
+ "%s: access report failed for %{public}@: %{public}@"
+ "%s: could not create the access store for %{public}@, no access count"
+ "%s: last drain for %{public}@ is %.0fs in the future, ignoring the throttle"
+ "%s: no access report for %{public}s/%{public}s, deferring to a later unlock (%lu of %lu)"
+ "%s: no localized string for %{public}@; falling back to the countless sentence"
+ "%s: still no access report for %{public}s/%{public}s after %lu deferrals, showing the prompt without a count"
+ "%s: timed out waiting for the access report for %{public}@"
+ "+[TCCDReminderMonitor milestoneOverrideFromDefaultsForKey:]"
+ "-[TCCDReminderMonitor enqueueReminderWithContext:deferrals:]"
+ "-[TCCDReminderMonitor healthDataAccessCountForBundleIdentifier:]"
+ "-[TCCDReminderMonitor healthDataAccessCountForBundleIdentifier:]_block_invoke"
+ "-[TCCDReminderMonitor isServiceThrottled:atTime:]"
+ "-[TCCDReminderMonitor reminderInfoTextForService:accessCount:]"
+ "-[TCCDReminderMonitor reportResourceUsage:]_block_invoke"
+ "-[TCCDReminderMonitor showReminderPrompt:result:accessCount:]"
+ "A\""
+ "HKDataTypeAccessStore"
+ "REMINDER_ACCESS_INFO_COUNT"
+ "REMINDER_ACCESS_INFO_COUNT_ONE"
+ "T@\"NSArray\",C,N,V_researchMilestoneOverride"
+ "T@\"NSString\",&,N,V_reminderAccessCountFormatLocalizationKey"
+ "T@\"NSString\",&,N,V_reminderAccessCountSingularLocalizationKey"
+ "_reminderAccessCountFormatLocalizationKey"
+ "_reminderAccessCountSingularLocalizationKey"
+ "_researchMilestoneOverride"
+ "accessCount"
+ "com.apple.developer.healthkit.research"
+ "deferrals"
+ "enqueueReminderWithContext:deferrals:"
+ "fetchAccessReportForBundleIdentifier:objectTypes:since:modeMask:completion:"
+ "healthAccessCountForContext:client:"
+ "healthDataAccessCountForBundleIdentifier:"
+ "healthResearchReminderMilestoneOverride"
+ "localizedStringFromNumber:numberStyle:"
+ "milestoneOverrideFromDefaultsForKey:"
+ "reminderAccessCountFormatLocalizationKey"
+ "reminderAccessCountFormatLocalizationKeyNameForServiceName:"
+ "reminderAccessCountSingularLocalizationKey"
+ "reminderAccessCountSingularLocalizationKeyNameForServiceName:"
+ "reminderInfoTextForService:accessCount:"
+ "researchMilestoneOverride"
+ "setReminderAccessCountFormatLocalizationKey:"
+ "setReminderAccessCountSingularLocalizationKey:"
+ "setResearchMilestoneOverride:"
+ "showReminderPrompt:result:accessCount:"
+ "v24@?0@\"HKDataTypeAccessReport\"8@\"NSError\"16"
+ "\xf0\xf0\xf0\xf0!\xf0c"
- "+[TCCDReminderMonitor milestoneOverrideFromDefaults]"
- "-[TCCDReminderMonitor enqueueReminderWithContext:]"
- "-[TCCDReminderMonitor reportResourceUsage:]_block_invoke_2"
- "-[TCCDReminderMonitor showReminderPrompt:result:]"
- "A!"
- "milestoneOverrideFromDefaults"
- "\xf0\xf0\xf0\xf1\xf0c"
```
