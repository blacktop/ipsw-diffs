## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1934.2.1.0.0
-  __TEXT.__text: 0x14c3c4
+1934.2.3.0.0
+  __TEXT.__text: 0x14cae8
   __TEXT.__auth_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0x155d4
+  __TEXT.__objc_methlist: 0x155ec
   __TEXT.__const: 0xe68
-  __TEXT.__cstring: 0xb96e
-  __TEXT.__oslogstring: 0xe23e
+  __TEXT.__cstring: 0xb98e
+  __TEXT.__oslogstring: 0xe2fe
   __TEXT.__gcc_except_tab: 0x3a2c
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__ustring: 0x1a0

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x5448
+  __TEXT.__unwind_info: 0x5458
   __TEXT.__eh_frame: 0x3a0
-  __TEXT.__objc_classname: 0x1af1
-  __TEXT.__objc_methname: 0x2eaa0
-  __TEXT.__objc_methtype: 0x48ff
-  __TEXT.__objc_stubs: 0x20fa0
+  __TEXT.__objc_classname: 0x1b07
+  __TEXT.__objc_methname: 0x2eb5d
+  __TEXT.__objc_methtype: 0x4921
+  __TEXT.__objc_stubs: 0x210a0
   __DATA_CONST.__got: 0x1778
   __DATA_CONST.__const: 0x4788
   __DATA_CONST.__objc_classlist: 0x760
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaba0
+  __DATA_CONST.__objc_selrefs: 0xabe0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x5d8
   __AUTH_CONST.__auth_got: 0xd30
-  __AUTH_CONST.__const: 0x2288
-  __AUTH_CONST.__cfstring: 0x9ca0
+  __AUTH_CONST.__const: 0x22a8
+  __AUTH_CONST.__cfstring: 0x9d40
   __AUTH_CONST.__objc_const: 0x17548
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4F197F1B-3F58-3236-B92B-54CA1DF97712
-  Functions: 8999
-  Symbols:   27098
-  CStrings:  11541
+  UUID: A1F0BAD0-2ECD-3ACC-905B-3F91DAF50C05
+  Functions: 9002
+  Symbols:   27113
+  CStrings:  11568
 
Symbols:
+ +[EKEventStore(iCloudReplyURLParsing) _parseiCloudReplyURL:reply:uid:]
+ -[EKEventStore(iCloudReplyURLParsing) eventForiCloudReplyURL:reply:]
+ __OBJC_$_CLASS_METHODS_EKEventStore(iCloudReplyURLParsing|Reminders)
+ __OBJC_$_INSTANCE_METHODS_EKEventStore(iCloudReplyURLParsing|Reminders)
+ ___68-[EKEventStore(iCloudReplyURLParsing) eventForiCloudReplyURL:reply:]_block_invoke
+ _objc_msgSend$_parseiCloudReplyURL:reply:uid:
+ _objc_msgSend$allEventsWithUniqueId:occurrenceDate:
+ _objc_msgSend$fragment
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$queryItems
+ _objc_msgSend$setQuery:
- __OBJC_$_CLASS_METHODS_EKEventStore
- __OBJC_$_INSTANCE_METHODS_EKEventStore(Reminders)
CStrings:
+ "%lu events for uid %@ allow participation status modifications"
+ "@32@0:8@16^Q24"
+ "B40@0:8@16^Q24^@32"
+ "Couldn't parse URL: %@"
+ "Found %lu unfiltered events for uid %@"
+ "Malformed UID data in URL"
+ "UID could not be decoded"
+ "URL missing uid"
+ "_parseiCloudReplyURL:reply:uid:"
+ "accept"
+ "decline"
+ "eventForiCloudReplyURL:reply:"
+ "fragment"
+ "iCloudReplyURLParsing"
+ "initWithBase64EncodedString:options:"
+ "initWithData:encoding:"
+ "initWithURL:resolvingAgainstBaseURL:"
+ "queryItems"
+ "reply"
+ "setQuery:"
+ "tentative"

```
