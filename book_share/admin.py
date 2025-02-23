from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 管理画面のリスト表示で表示する項目
    list_display = ('content', 'user', 'created_at', 'book_title', 'book_author')
    
    # フィルタ機能を使うフィールド
    list_filter = ('user', 'created_at')
    
    # 検索可能なフィールド
    search_fields = ('content', 'book_title', 'book_author')
    
    # デフォルトの並び順
    ordering = ('-created_at',)
    
    # 日付階層ナビゲーション
    date_hierarchy = 'created_at'
    
    # 管理画面でのフィールドセット構成
    fieldsets = (
        ('投稿情報', {
            'fields': ('user', 'image', 'content')
        }),
        ('書籍情報', {
            'fields': ('book_title', 'book_author'),
            'classes': ('collapse',),  # 折りたたみ可能に設定
        }),
    )
