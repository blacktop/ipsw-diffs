# 18.1 (22B82) .vs 18.1.1 (22B91)

## IPSWs

- `iPhone17,1_18.1_22B82_Restore.ipsw`
- `iPhone17,1_18.1.1_22B91_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.1 *(22B82)* | 24.1.0 | 11215.42.1~1 | Mon, 07Oct2024 21:14:29 PDT |
| 18.1.1 *(22B91)* | 24.1.0 | 11215.42.1~1 | Mon, 07Oct2024 21:14:29 PDT |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### SafariWidgetExtension

>  `/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension`

```diff

-7619.2.8.10.7
+7619.2.8.10.9
   __TEXT.__text: 0x4ad88
   __TEXT.__auth_stubs: 0x1520
   __TEXT.__cstring: 0x2f2a

   __TEXT.__eh_frame: 0x1d14
   __DATA_CONST.__auth_got: 0xa90
   __DATA_CONST.__got: 0x530
-  __DATA_CONST.__auth_ptr: 0xc70
+  __DATA_CONST.__auth_ptr: 0xc48
   __DATA_CONST.__const: 0x1748
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.1 *(22B82)* | 619.2.8.10.7 |
| 18.1.1 *(22B91)* | 619.2.8.10.9 |

### Dylibs

#### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### WebKit

>  `/System/Library/Frameworks/WebKit.framework/WebKit`

```diff

-619.2.8.10.7
-  __TEXT.__text: 0xe592f4
+619.2.8.10.9
+  __TEXT.__text: 0xe59498
   __TEXT.__auth_stubs: 0x16d70
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x14254

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 63683
-  Symbols:   76712
+  Functions: 63681
+  Symbols:   76711
   CStrings:  25718
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1026: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1393: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1543: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 789: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 809: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 833: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 850: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 864: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 896: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 937: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 939: Invalid message dispatched %s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 994: Invalid message dispatched %s"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1002: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1368: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1518: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 788: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 805: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 826: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 840: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 851: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 880: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 897: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 917: Invalid message dispatched %s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 970: Invalid message dispatched %s"

```

#### AuthenticationServicesCore

>  `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-619.2.8.10.7
+619.2.8.10.9
   __TEXT.__text: 0xb634c
   __TEXT.__auth_stubs: 0x2280
   __TEXT.__objc_methlist: 0x2618

   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1150
-  __AUTH_CONST.__auth_ptr: 0x6c0
+  __AUTH_CONST.__auth_ptr: 0x6b0
   __AUTH_CONST.__const: 0x50b8
   __AUTH_CONST.__cfstring: 0x1d80
   __AUTH_CONST.__objc_const: 0x7880

```

#### MobileSafari

>  `/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari`

```diff

-619.2.8.10.7
+619.2.8.10.9
   __TEXT.__text: 0x3924b8
   __TEXT.__auth_stubs: 0x4480
   __TEXT.__objc_methlist: 0x11cec

   __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0x258
   __AUTH_CONST.__auth_got: 0x2258
-  __AUTH_CONST.__auth_ptr: 0x1f20
+  __AUTH_CONST.__auth_ptr: 0x1ef8
   __AUTH_CONST.__const: 0x12890
   __AUTH_CONST.__cfstring: 0x8480
   __AUTH_CONST.__objc_const: 0x31ea8

```

#### PasswordManagerUI

>  `/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI`

```diff

-7619.2.8.10.7
+7619.2.8.10.9
   __TEXT.__text: 0x3ef17c
   __TEXT.__auth_stubs: 0x57d0
   __TEXT.__objc_methlist: 0x14c0

   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x2bf8
-  __AUTH_CONST.__auth_ptr: 0x3d70
+  __AUTH_CONST.__auth_ptr: 0x3c40
   __AUTH_CONST.__const: 0x12a98
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x9bd8

```

#### JavaScriptCore

>  `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-619.2.8.10.7
-  __TEXT.__text: 0x15c0fd8
+619.2.8.10.9
+  __TEXT.__text: 0x15c1158
   __TEXT.__jsc_int: 0x7749c
   __TEXT.__auth_stubs: 0x2d30
   __TEXT.__objc_methlist: 0x9cc
CStrings:
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/LazyRef.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/fd45e0a1-a2ae-11ef-9cba-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/LazyRef.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"

```


</details>

## EOF
