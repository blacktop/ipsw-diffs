## ProximityReader

> `/System/Library/Frameworks/ProximityReader.framework/ProximityReader`

```diff

-134.20.0.0.0
-  __TEXT.__text: 0x8fa2c
+135.1.0.0.0
+  __TEXT.__text: 0x8ebc4
   __TEXT.__auth_stubs: 0x24c0
   __TEXT.__objc_methlist: 0x470
-  __TEXT.__const: 0x4582
-  __TEXT.__cstring: 0x483c
-  __TEXT.__swift5_typeref: 0x1d40
-  __TEXT.__swift5_reflstr: 0x2002
+  __TEXT.__const: 0x4562
+  __TEXT.__cstring: 0x47bc
+  __TEXT.__swift5_typeref: 0x1d38
+  __TEXT.__swift5_reflstr: 0x2012
   __TEXT.__swift5_assocty: 0x2c0
   __TEXT.__constg_swiftt: 0x18ec
   __TEXT.__swift5_fieldmd: 0x1d70
   __TEXT.__swift5_proto: 0x2b4
   __TEXT.__swift5_types: 0x1c4
-  __TEXT.__oslogstring: 0x2138
-  __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0x810
+  __TEXT.__oslogstring: 0x20a2
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift_as_entry: 0x22c
   __TEXT.__swift_as_ret: 0x24c
+  __TEXT.__swift5_capture: 0x810
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2830
-  __TEXT.__eh_frame: 0x5810
+  __TEXT.__swift5_protos: 0x10
+  __TEXT.__unwind_info: 0x2bd0
+  __TEXT.__eh_frame: 0x56e0
   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0xff3
   __TEXT.__objc_methtype: 0x100
   __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__got: 0x740
   __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_selrefs: 0x580
   __DATA_CONST.__objc_protorefs: 0x40
   __AUTH_CONST.__auth_got: 0x1268
-  __AUTH_CONST.__auth_ptr: 0x868
+  __AUTH_CONST.__auth_ptr: 0x850
   __AUTH_CONST.__const: 0x38c0
   __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0x16e8
   __AUTH.__objc_data: 0x4f8
   __AUTH.__data: 0x2358
-  __DATA.__data: 0x1228
-  __DATA.__bss: 0x6040
-  __DATA.__common: 0xa9
+  __DATA.__data: 0x1220
+  __DATA.__bss: 0x6030
+  __DATA.__common: 0x79
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2928
-  Symbols:   1253
-  CStrings:  796
+  Functions: 2921
+  Symbols:   1251
+  CStrings:  787
 
Symbols:
- _objc_release_x28
- _symbolic _____m 15ProximityReader011PaymentCardB0C
CStrings:
+ "%{public}s.%{public}s"
+ "Closed by remote?=%{bool,public}d"
+ "Error (%s: %{public}@"
+ "Error (%s: a previous request is running, returning busy"
+ "Error (%s: proxy error handler [ %s ]"
+ "Error (%s: unexpected error [ %s ]"
+ "Error (%s: unexpected proxy type"
+ "Error (capturePIN): %{public}s"
+ "Error (closeSession): proxy error handler [ %s ]"
+ "Error (closeSession): unexpected proxy type"
+ "Error (isAccountLinked): %{public}s"
+ "Error (linkAccount): %{public}s"
+ "Error (prepare): %{public}s"
+ "Error (prepare): unexpected session type"
+ "Error (prepare): unknown"
+ "Error (read): %{public}s"
+ "Error (readerIdentifier): %{public}s"
+ "Error (refreshContext): isRead = %{bool,public}d, failed"
+ "Error (refreshContext): proxy error handler [ %s ]"
+ "Error (refreshContext): unexpected proxy type"
+ "Error (status): %{public}s"
+ "Error (storeAndForwardDecline): %{public}s"
+ "Error (storeAndForwardDecline): unexpected error [ %s ]"
+ "Error (storeAndForwardStatus): %{public}s"
+ "Error (storeAndForwardStatus): unexpected error [ %s ]"
+ "Going to background, disconnecting"
+ "No VAS merchant provided"
+ "OS deprecation date: %{public}s"
+ "PIN capture is not supported during a SAF session"
+ "PIN token is empty"
+ "PaymentCardReader.isSupported: %{bool,public}d"
+ "Result (cancelRead): %{bool,public}d"
+ "Result (fetchStoredPaymentCardReadResultBatch): success"
+ "Result (fetchStoredPaymentCardReadResultCount): success"
+ "Result (isAccountLinked): %{bool,public}d"
+ "Result (read): success"
+ "Result (readerIdentifier): %{public}s"
+ "Result (refreshContext): success"
+ "Result (resetBatchState): success"
+ "Result (resolveBatch): success"
+ "Result (storeAndForwardDecline): success"
+ "Result (storeAndForwardStatus): success"
+ "Session is wrong, nil or invalidated [ %s ]"
+ "Transaction ID is invalid"
+ "Transactions received [%ld] do not match the requested [%ld]"
+ "Unknown store error: %@"
+ "Unknown transaction data type [ %ld ]"
+ "Warning (%s: backgroundRequestNotAllowed"
+ "Warning (%s: readFromBackgroundError"
+ "XPC service disconnected"
+ "added eventHandlers=%{public}ld"
+ "added updateHandlers=%{public}ld"
+ "closing session with delete=%{bool,public}d"
+ "events stream cancelled"
+ "last reader removed, releasing connection"
+ "prepareStoreAndForward()"
+ "readerFeedback: %{public}s, eventHandlers count=%{public}ld"
+ "readerIdentifier retrieved from cache"
+ "removed eventHandlers=%{public}ld"
+ "removed updateHandlers=%{public}ld"
- "%{private}s.%{private}s"
- "AID validated - %{private}s"
- "Application not in foreground, returning from %s"
- "Application not in foreground, returning from [%s]"
- "Attempting to access %s - Not Supported"
- "Calling capturePIN in a SAF session, not supported"
- "Error (%s): [%@]"
- "Error (%s): a previous request is running, returning busy"
- "Error (%s): a previous store request is running, returning busy"
- "Error (%s): proxy error handler: %@"
- "Error (%s): unexpected error received: [%@]"
- "Error (%s): unexpected error type"
- "Error (capturePIN): %s"
- "Error (context): Unexpected error type"
- "Error (context): isRead = %{bool}d, %@"
- "Error (context): isRead = %{bool}d, ReadError.readNotAllowed"
- "Error (decline): %@"
- "Error (decline): unexpected error [%@]"
- "Error (isAccountLinked): %s"
- "Error (linkAccount): %s"
- "Error (prepare): %s"
- "Error (prepare): ErrorDetails.unknownSessionError"
- "Error (read): %s"
- "Error (readerIdentifier): %s"
- "Error (status): %s"
- "Error (storeAndForwardStatus): %@"
- "Error (storeAndForwardStatus): unexpected error [%@]"
- "Error while closing reader session"
- "Going to background, disconnect"
- "OS deprecation date: %s"
- "PIN token invalid! PIN Token empty."
- "PIN transaction ID is invalid"
- "PaymentCardReadResult - %@"
- "PaymentCardReader destroyed"
- "PaymentCardReaderSession destroyed"
- "PaymentTerminalServiceDelegate.closed(), remote?=%{bool}d"
- "Result (cancelRead): result = %{bool}d"
- "Result (context): context created"
- "Result (isAccountLinked): returned %{bool}d"
- "Result (prepare): Unexpected session type"
- "Result (read): success with result"
- "Result (readerIdentifier): success %s"
- "Result (storeAndForwardStatus): %@"
- "Returning batch result with [%ld] transactions"
- "Service XPC disconnected"
- "Session is wrong, nil or invalidated [%s]"
- "Success (decline): Transaction declined"
- "Transactions received[%ld] do not match the requested[%ld]"
- "Unknown StoreErrorInternal: %@"
- "Unknown transaction data type [%ld]"
- "User cancelled"
- "added eventHandlers=%ld"
- "added updateHandlers=%ld"
- "cancel transaction"
- "closeSession | remote proxy error handler: %@"
- "closeSession | remote proxy was not of expected type"
- "closing session with delete=%{bool}d"
- "getTerminalId() - retrieve from cache"
- "no VAS merchant provided"
- "prepare(using:options:)"
- "prepare(using:options:updateHandler:)"
- "prepareStoreAndForward(options:)"
- "read(_:_:eventHandler:)"
- "reader Last reader removed, release connection"
- "readerFeedback: %s, eventHandlers count=%ld"
- "refreshContext | remote proxy error handler: %@"
- "removed eventHandlers=%ld"
- "removed updateHandlers=%ld"

```
