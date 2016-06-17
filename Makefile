TA_DEV_KIT_DIR := ../../export-user_ta/
CROSS_COMPILE := arm-linux-gnueabihf-
CFG_TEE_TA_LOG_LEVEL ?= 2
CPPFLAGS += -DCFG_TEE_TA_LOG_LEVEL=$(CFG_TEE_TA_LOG_LEVEL)
BINARY=534d4152-5443-534c-5444415441535431
TA_ROOT := .
include $(TA_DEV_KIT_DIR)/mk/ta_dev_kit.mk 
all: $(BINARY).ta 
$(BINARY).ta: $(BINARY).bin
	rm -f $@ 
	cat faked_armv7_uta_signed_header.bin $< > $@
clean: clean_ta_file
.PHONY: clean_ta_file
clean_ta_file:
	rm -f $(BINARY).ta
