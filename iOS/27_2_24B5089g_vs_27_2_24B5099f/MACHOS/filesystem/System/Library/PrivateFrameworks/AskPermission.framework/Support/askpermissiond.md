## askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-130.1.4.0.0
-  __TEXT.__text: 0x5160c
+130.1.6.0.0
+  __TEXT.__text: 0x52c18
   __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_stubs: 0x5a00
-  __TEXT.__objc_methlist: 0x29dc
+  __TEXT.__objc_stubs: 0x5bc0
+  __TEXT.__objc_methlist: 0x2a8c
   __TEXT.__const: 0x660
-  __TEXT.__cstring: 0x3394
+  __TEXT.__cstring: 0x3434
   __TEXT.__objc_classname: 0x61b
-  __TEXT.__objc_methname: 0x6f06
-  __TEXT.__oslogstring: 0x5b04
-  __TEXT.__objc_methtype: 0x1749
+  __TEXT.__objc_methname: 0x7156
+  __TEXT.__oslogstring: 0x5e04
+  __TEXT.__objc_methtype: 0x17a9
   __TEXT.__gcc_except_tab: 0x380
   __TEXT.__swift5_typeref: 0x319
   __TEXT.__swift5_capture: 0x36c

   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0x70
-  __TEXT.__unwind_info: 0xe98
+  __TEXT.__unwind_info: 0xec0
   __TEXT.__eh_frame: 0xb88
-  __DATA_CONST.__const: 0x1968
-  __DATA_CONST.__cfstring: 0x3240
+  __DATA_CONST.__const: 0x1988
+  __DATA_CONST.__cfstring: 0x3340
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x9e8
-  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA.__objc_const: 0x5620
-  __DATA.__objc_selrefs: 0x1a50
-  __DATA.__objc_ivar: 0x364
+  __DATA.__objc_const: 0x57c8
+  __DATA.__objc_selrefs: 0x1ac0
+  __DATA.__objc_ivar: 0x384
   __DATA.__objc_data: 0x1490
   __DATA.__data: 0x690
   __DATA.__crash_info: 0x148

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1167
-  Symbols:   555
-  CStrings:  2170
+  Functions: 1185
+  Symbols:   557
+  CStrings:  2213
 
Symbols:
+ _AMSAccountMediaTypeAppStoreSandbox
+ _OBJC_CLASS_$_NSISO8601DateFormatter
CStrings:
+ "%{public}@: Failed to handle Sandbox remote notification. Error: %{public}@"
+ "%{public}@: Getting SANDBOX Store Accounts"
+ "%{public}@: Getting Sandbox user. Action: %{public}ld"
+ "%{public}@: Handled Sandbox remote notification succesfully"
+ "%{public}@: Handling Sandbox request in Pending state"
+ "%{public}@: Handling Sandbox request in Unknown state"
+ "%{public}@: Ignoring pending request."
+ "%{public}@: Missing server result - %{public}@"
+ "%{public}@: No active Sandbox account"
+ "%{public}@: No sandbox store accounts"
+ "%{public}@: No store OR sandbox accounts - will not progress any further"
+ "%{public}@: Payload missing request DSID - will not progress any further"
+ "%{public}@: Payload request DSID doesn't match any active store or sandbox DSIDs - will not progress any further"
+ "%{public}@: Starting requester remote notification task (Sandbox: %d). Payload: %{public}@"
+ "%{public}@: Unable to decode server result - %{public}@"
+ "@240@0:8@16@24@32@40@48@56@64@72@80@88B96B100@104@112@120@128@136@144@152@160@168B176@180@188@196q204B212@216@224@232"
+ "@28@0:8^@16B24"
+ "@36@0:8@16B24^@28"
+ "@36@0:8q16B24^@28"
+ "@40@0:8@16@24B32B36"
+ "@76@0:8@16@24@32B40@44@52@60q68"
+ "ISO8601DateFormatter"
+ "No active Sandbox account"
+ "Server Response Error"
+ "T@\"NSNumber\",R,N,V_requesterDSID"
+ "TB,N,V_isSandbox"
+ "TB,R,N,V_isSandbox"
+ "Unable to decode server result"
+ "_activeSandboxStoreDSIDs"
+ "_handleRequesterNotification:withRequesterDSID:andSuppressDialog:"
+ "_handleSandboxNotification:withRequesterDSID:"
+ "_handleSandboxRequest"
+ "_isSandbox"
+ "_requestInfoForIndentifier:isSandbox:withError:"
+ "_serverRequestWithError:isSandbox:"
+ "_serverRequestWithUser:isSandbox:error:"
+ "ams_iTunesSandboxAccounts"
+ "approvalRequestWithRequestIdentifier:isSandbox:"
+ "bagForProfile:profileVersion:processInfo:"
+ "createdDateISO8601"
+ "dateFormatter"
+ "initWithDate:requestIdentifier:uniqueIdentifier:isSandbox:itemIdentifier:localizations:offerName:status:"
+ "initWithItemIdentifier:requestIdentifier:uniqueIdentifier:ageRating:ageRatingValue:approverDSID:requesterDSID:requesterAltDSID:createdDate:modifiedDate:isException:isSandbox:itemBundleID:itemDesc:itemTitle:localizedPrice:previewURL:productType:productTypeName:productURL:offerName:originatedOnThisDevice:requestString:requestSummary:priceSummary:status:suppressClientResume:starRating:thumbnailURLString:uuid:"
+ "initWithPayload:requesterDSID:isSandbox:andSuppressDialog:"
+ "is-sandbox"
+ "isSandbox"
+ "isSandboxRequest"
+ "modifiedDateISO8601"
+ "primaryiCloudUserWithAction:isSandbox:keychainError:"
+ "sandboxBag"
+ "setFormatOptions:"
+ "setIsSandbox:"
+ "v36@0:8@16@24B32"
- "%{public}@: Payload request DSID doesn't match store DSIDs: %@"
- "%{public}@: Starting requester remote notification task. Payload: %{public}@"
- "@236@0:8@16@24@32@40@48@56@64@72@80@88B96@100@108@116@124@132@140@148@156@164B172@176@184@192q200B208@212@220@228"
- "@72@0:8@16@24@32@40@48@56q64"
- "_handleRequesterNotification:andSuppressDialog:"
- "_serverRequestWithUser:error:"
- "initWithDate:requestIdentifier:uniqueIdentifier:itemIdentifier:localizations:offerName:status:"
- "initWithItemIdentifier:requestIdentifier:uniqueIdentifier:ageRating:ageRatingValue:approverDSID:requesterDSID:requesterAltDSID:createdDate:modifiedDate:isException:itemBundleID:itemDesc:itemTitle:localizedPrice:previewURL:productType:productTypeName:productURL:offerName:originatedOnThisDevice:requestString:requestSummary:priceSummary:status:suppressClientResume:starRating:thumbnailURLString:uuid:"
- "initWithPayload:andSuppressDialog:"
- "primaryiCloudUserWithAction:keychainError:"
```
