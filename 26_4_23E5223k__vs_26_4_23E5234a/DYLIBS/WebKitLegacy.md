## WebKitLegacy

> `/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`

```diff

-624.1.14.10.4
-  __TEXT.__text: 0x15dfbc
+624.1.16.10.6
+  __TEXT.__text: 0x15e19c
   __TEXT.__auth_stubs: 0x8d90
   __TEXT.__objc_methlist: 0xf610
   __TEXT.__const: 0x220

   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x46e0
-  __AUTH_CONST.__const: 0x5220
+  __AUTH_CONST.__const: 0x5228
   __AUTH_CONST.__cfstring: 0xf020
   __AUTH_CONST.__objc_const: 0xfe80
   __AUTH_CONST.__objc_intobj: 0x2d0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F67B4140-8FD2-3114-BDD2-67C26E0847A9
+  UUID: 3135A515-783C-3E34-92A2-B73EF3A12DFA
   Functions: 7302
-  Symbols:   23687
+  Symbols:   23689
   CStrings:  9592
 
Symbols:
+ __ZZN3WTF16secureMemsetSpanIyLm18446744073709551615EEEvNSt3__14spanIT_XT0_EEEhE9memsetPtr
+ _memset
Functions:
~ -[DOMRGBColor color] : 260 -> 288
~ __ZN7WebCore5ColorD2Ev : 100 -> 116
~ -[WebFrame(WebInternal) _updateBackgroundAndUpdatesWhileOffscreen] : 496 -> 524
~ -[WebFrame(WebPrivate) _bodyBackgroundColor] : 348 -> 360
~ -[WebFrame(WebPrivate) setCaretColor:] : 192 -> 208
~ -[WebFrame(WebPrivate) caretColor] : 464 -> 496
~ -[WebFrame(WebPrivate) setMarkedText:selectedRange:] : 972 -> 788
~ __ZN3WTF6VectorIN7WebCore20CompositionHighlightELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEED2Ev : 300 -> 328
~ __ZN3WTF6VectorIN7WebCore20CompositionUnderlineELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEED1Ev : 176 -> 188
~ -[WebFrame(WebPrivate) setMarkedText:forCandidates:] : 820 -> 644
~ -[WebFrameView drawRect:] : 320 -> 348
~ -[WebHTMLView(WebNSTextInputSupport) setMarkedText:selectedRange:] : 888 -> 956
~ __ZN7WebCore15KeypressCommandD2Ev : 444 -> 520
~ -[WebUITextIndicatorData(WebUITextIndicatorInternal) initWithImage:textIndicator:scale:] : 1284 -> 1312
~ -[WebView(WebPrivate) _commonInitializationWithFrameName:groupName:] : 9552 -> 9580
~ -[WebView(WebPrivate) initSimpleHTMLDocumentWithStyle:frame:preferences:groupName:] : 8140 -> 8168
~ __ZN7WebCore14FontAttributesD2Ev : 372 -> 444
~ -[WebIndicateLayer initWithWebView:] : 312 -> 320
~ __ZN3WTF6VectorIN7WebCore21InspectorOverlayLabelELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEED1Ev : 376 -> 472
~ __ZN7WebCore25InspectorOverlayHighlightD2Ev : 860 -> 1040
~ -[WebPDFView drawPage:] : 604 -> 632
~ -[WebPlainWhiteView drawRect:] : 220 -> 248
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StyleScrollbarWidth.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/Box.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/WeakRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdJugCeU8QHRsFfq5BP2U5auRH23ONT0HRkP08/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StyleScrollbarWidth.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/Box.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/WeakRef.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8LugA5aCWGhLtUREyV8ychiHgYBqzovhoJa74/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"

```
