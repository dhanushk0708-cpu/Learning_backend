"""
=========================================
PHASE 2

TOPIC : FILE UPLOAD
=========================================

USED IN

app/routers/

"""

from fastapi import UploadFile, File

# WHY?
# Upload files like
# Images
# PDFs
# Documents
# Videos

# CIVIL AI IMPLEMENTATION


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    return {"filename": file.filename}


# CONCEPT

# UploadFile

# ↓

# Receives Uploaded File

# ↓

# Read / Save / Process File

# INTERNAL FLOW

# React

# ↓ Upload File

# FastAPI

# ↓

# UploadFile

# ↓

# Save File

# ↓

# Response

# INTERVIEW

# Q: Why use UploadFile instead of bytes?
#
# A:
# UploadFile is memory efficient
# and suitable for large files.

# COMMON BEGINNER MISTAKE

# ❌ Reading entire file
# into memory.

# ✅ Use UploadFile.

# RELATED CONCEPTS

# File Upload

# ↓

# Storage

# ↓

# Database

# REMEMBER

# ✔ UploadFile
# ✔ File(...)
# ✔ Better for Large Files
