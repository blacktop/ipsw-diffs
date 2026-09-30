## EventKitDataConsumer

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Versions/A/DataConsumers/EventKitDataConsumer.dataconsumer/Contents/MacOS/EventKitDataConsumer`

```diff

-  __TEXT.__text: 0x10ab4
+  __TEXT.__text: 0x11580
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x4840
-  __TEXT.__objc_methlist: 0x7cc
-  __TEXT.__const: 0x188
-  __TEXT.__objc_methname: 0x3ca8
-  __TEXT.__cstring: 0x130
+  __TEXT.__objc_stubs: 0x4940
+  __TEXT.__objc_methlist: 0x814
+  __TEXT.__const: 0x1b0
+  __TEXT.__objc_methname: 0x3e27
+  __TEXT.__cstring: 0x143
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methtype: 0x480
+  __TEXT.__objc_methtype: 0x4c5
   __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__oslogstring: 0x1dc1
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__oslogstring: 0x202f
+  __TEXT.__unwind_info: 0x258
   __DATA_CONST.__const: 0x140
-  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0x1f8
-  __DATA.__objc_const: 0x8b8
-  __DATA.__objc_selrefs: 0x1388
+  __DATA_CONST.__got: 0x220
+  __DATA.__objc_const: 0x8c0
+  __DATA.__objc_selrefs: 0x13d0
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 201
-  Symbols:   118
-  CStrings:  855
+  Functions: 207
+  Symbols:   122
+  CStrings:  876
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_EKSyncError
+ _OBJC_CLASS_$_NSDictionary
+ _kEKCalendarItemErrorOptimisticallyClearForChangesToKeys
+ _kEKCalendarItemErrorPropertyNameAttachments
CStrings:
+ "[%{public}@] %{public}@ interim commit before detached items failed: %{private}@"
+ "[%{public}@] missing EKEvent for unconsumed attendee change [%{private}@]"
+ "_buildAttendeeOnlyChangeItemForEvent:withAttendeeProperties:accountID:"
+ "_eventKitCalendarItemErrorCodeFromKind:"
+ "_findExistingDetachmentInParent:matchingOriginalDate:"
+ "_originalStartDateForDetachedChangeItemProperties:"
+ "allowsContentModifications"
+ "attachmentTooLarge"
+ "dictionaryWithObjects:forKeys:count:"
+ "initWithCalendarItemError:userInfo:"
+ "itemDidFailToSync ignored for non-event itemType=%ld (externalID=%{public}@)"
+ "itemDidFailToSync: failed to save syncError on '%{private}@' err=%{private}@"
+ "itemDidFailToSync: no EKCalendarItemError mapping for kind=%{public}@; underlying=%{private}@"
+ "itemDidFailToSync: no EKEvent for externalID=%{public}@; skipping"
+ "itemDidFailToSync: skipping immutable calendar for event '%{private}@'"
+ "itemDidFailToSync: stamped syncError (%ld) on '%{private}@' externalID=%{public}@"
+ "itemDidFailToSyncWithExternalID:itemType:kind:error:"
+ "setSyncError:"
+ "v48@0:8@\"NSString\"16q24@\"NSString\"32@\"NSError\"40"
+ "v48@0:8@16q24@32@40"

```
