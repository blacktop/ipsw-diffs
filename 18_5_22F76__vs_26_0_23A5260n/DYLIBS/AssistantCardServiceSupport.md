## AssistantCardServiceSupport

> `/System/Library/PrivateFrameworks/AssistantCardServiceSupport.framework/AssistantCardServiceSupport`

```diff

-3405.30.3.11.5
+3500.74.4.1.2
   __TEXT.__text: 0x449c
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x220
   __TEXT.__oslogstring: 0x39
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__unwind_info: 0x120
   __TEXT.__objc_classname: 0xa4
   __TEXT.__objc_methname: 0xd52
   __TEXT.__objc_methtype: 0x185

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EEA6A63B-EDA4-3454-A7C4-7E6975CBEA4B
+  UUID: B7540E63-DE7E-3465-ACCB-5E80B735FA3B
   Functions: 58
   Symbols:   467
   CStrings:  285
Functions:
~ -[ACSCardService canSatisfyCardRequest:] -> -[INAddTasksIntent(ACSCardRequesting) requestCard:reply:] : 156 -> 1052
~ -[INAddTasksIntent(ACSCardRequesting) requestCard:reply:] -> ___57-[INAddTasksIntent(ACSCardRequesting) requestCard:reply:]_block_invoke : 1052 -> 548
~ ___57-[INAddTasksIntent(ACSCardRequesting) requestCard:reply:]_block_invoke -> -[INAddTasksIntent(ACSCardRequesting) servicePriorityForCardRequest:] : 548 -> 8
~ -[INCurrencyAmount(AssistantCardService) acs_formattedAmountString] -> -[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:] : 8 -> 248
~ -[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:] -> ___76-[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:]_block_invoke : 248 -> 116
~ ___76-[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:]_block_invoke -> -[INCurrencyAmount(AssistantCardService) _acs_currencySymbol] : 116 -> 92
~ -[INCurrencyAmount(AssistantCardService) _acs_currencySymbol] -> +[INCurrencyAmount(AssistantCardService) _acs_localeForCode:] : 92 -> 376
~ +[INCurrencyAmount(AssistantCardService) _acs_localeForCode:] -> +[INCurrencyAmount(AssistantCardService) _acs_currencySymbolForCode:] : 376 -> 212
~ +[INCurrencyAmount(AssistantCardService) _acs_currencySymbolForCode:] -> -[ACSCardService canSatisfyCardRequest:] : 212 -> 156

```
