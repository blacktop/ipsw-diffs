## AskPermission

> `/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission`

```diff

-129.0.23.0.0
-  __TEXT.__text: 0x9808
+129.0.25.0.0
+  __TEXT.__text: 0x9820
   __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_methlist: 0xa0c
   __TEXT.__const: 0xea
   __TEXT.__gcc_except_tab: 0x37c
   __TEXT.__cstring: 0x788
-  __TEXT.__oslogstring: 0xa88
+  __TEXT.__oslogstring: 0xaa1
   __TEXT.__swift5_typeref: 0x94
   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__unwind_info: 0x350
   __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x19c4
-  __TEXT.__objc_methtype: 0x54e
+  __TEXT.__objc_methname: 0x19d0
+  __TEXT.__objc_methtype: 0x556
   __TEXT.__objc_stubs: 0x1080
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x420

   __AUTH_CONST.__objc_const: 0x1090
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x2d0
   __DATA.__bss: 0x68
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 55492846-0273-34D9-A79E-A4F27A1BCC22
+  UUID: 2F3B3486-67CB-3CC2-97C8-5EC47750C865
   Functions: 230
   Symbols:   952
   CStrings:  623
Symbols:
+ +[APRequestHandler presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:isException:]
+ _objc_msgSend$presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:isException:
- +[APRequestHandler presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:]
- _objc_msgSend$presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:
Functions:
~ +[APRequestHandler presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:] -> +[APRequestHandler presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:isException:] : 584 -> 608
CStrings:
+ "%{public}@: Present product page. Title: %{public}@, body: %{public}@, itemIdentifier: %{public}@, previewURL: %{public}@, isException: %{public}d"
+ "presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:isException:"
+ "v100@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSString\"88B96"
+ "v100@0:8@16@24@32@40@48@56@64@72@80@88B96"
- "%{public}@: Present product page. Title: %{public}@, body: %{public}@, itemIdentifier: %{public}@, previewURL: %{public}@"
- "presentProductPageWithTitle:body:approve:decline:itemIdentifier:previewURL:offerName:requestString:requestSummary:priceSummary:"
- "v96@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSString\"88"
- "v96@0:8@16@24@32@40@48@56@64@72@80@88"

```
